---
title: Powershell and PSExec
date: 2022-05-17 21:39 +0200
categories: [Hunting, MDE]
tags: [mde, hunting, psexec, false positive]
---
{% include mermaid.liquid %}

Today we investigate some strange behaviour from a (possibly user) executed Powershell session.

## The Alert

![storyline](/assets/img/posts/2022-05-17/storyline_start.jpg)

Everything started with an explorer.exe running the following commandline.

```powershell
"cmd.exe" /c echo|set/p="C:\Temp\Tools"|powershell -NoP -W 1 -NonI -NoL "SaPs 'cmd' -Args '/c """cd /d',$([char]34+$Input+[char]34),'^&^& start /b cmd.exe"""' -Verb RunAs"
```

When explorer.exe starts something, this usually means that a user started this with a run command.
However, as there are ways to obfuscate this by for example running cmd like
this ```explorer.exe /root,"C:\Windows\System32\cmd.exe"```

Let's first inspect the commandline though, it seems to switch the execution path to C:\Temp\Tools and elevate to
administrative rights.
I always like to first get a handle on the parameters used to run powershell.

| Parameter | Parameter Full  | Explanation                                                                                     |
|:----------|:----------------|:------------------------------------------------------------------------------------------------|
| -NoP      | -NoProfile      | Who would do that? Doesn't really have a negative impact though                                 |
| -W 1      | -WindowStyle 1  | Strange param because usually one would see "Normal, Minimized, Maximized or Hidden" no numbers |
| -NonI     | -NonInteractive | Makes the session non interactive, which is of course interesting                               |
| -NoL      | -NoLogo         | Removes the Logo of session, no real impact                                                     |

The ```-W 1``` param is definitely fancy for me, usually one would expect ```-W Hidden```, but it seems like it
accomplishes the same job.

So far my verdict is, the user executed this process, which makes it more or less legitimate, but the params are
strange, so I cannot say a direct false or true positive right now.
Because of this, we need to dig deeper.

## Hunting deeper

In MDE we can also see the following alerts:
![alerts](/assets/img/posts/2022-05-17/alerts.jpg)

But there is exactly no information on why MDE thinks that there is suspicious discovery going on.
Because of this I decided to check if there were new processes spawned after the admin cmd.exe via advanced hunting.
For this we take the PID and timeframe of execution and of course the device the execution happened on.

Example script:

```powershell
let pid = "1234";
let device = "mydevice";
let time_span = datetime(2022-01-01T00:00:00);
DeviceProcessEvents
| where Timestamp between (time_span .. (time_span + 1d))
| where DeviceName contains device
| where ProcessId == pid or InitiatingProcessId == pid
| project Timestamp, FileName,
    ProcessCommandLine,
    InitiatingProcessCommandLine,
    ProcessId,
    InitiatingProcessId,
    InitiatingProcessParentId,
    ReportId
| order by Timestamp asc
```

This in the end gave me some interesting results.
![spawn1](/assets/img/posts/2022-05-17/spawn1.jpg)
We can see (in green) the parent process cmd.exe spawned two sub processes, once again cmd.exe and one
```conhost.exe 0xffffffff -ForceV1``` we will get back to conhost.exe later

Of course now I wanted to get an understanding of if this new cmd.exe started something, so I adjusted my hunting query
and tried again with this result:
![spawn2](/assets/img/posts/2022-05-17/spawn2.jpg)

## PsExec
The executed PsExec commands:

```cmd
PsExec.exe  \\mydevice -accepteula -nobanner -s cmd /c powershell.exe -noninteractive -command "&{Get-MPComputerStatus | Select-Object -Property AntispywareEnabled, AntivirusEnabled, OnAccessProtectionEnabled, RealTimeProtectionEnabled}"
PsExec.exe  \\mydevice -accepteula -nobanner -s cmd /c powershell.exe -noninteractive -command "&{Get-MPComputerStatus | Select-Object -Property AMServiceEnabled, AntispywareEnabled, AntispywareSignatureLastUpdated, AntivirusEnabled, AntivirusSignatureLastUpdated, BehaviorMonitorEnabled, IoavProtectionEnabled, NISEnabled, NISSignatureLastUpdated, OnAccessProtectionEnabled, RealTimeProtectionEnabled, TamperProtectionSource}"
```

Now we are getting somewhere, PSExec was executed, why this was not mentioned in the alert is beyond me. Goes to show
that you should not just blindly trust MDE to do its job.
But it definitely explains the "suspicious discovery" which MDE was talking about.
Reading the commands sent is quite easy, someone is trying to get information about the security status of this device.
So far the flow of process looks a bit like this:

<div class="mermaid">
flowchart TD;
    ex[explorer.exe\nRunning in user context];
    cmd1[cmd.exe\nRunning in user context];
    ps1[powershell.exe\nRunning in user context];
    cmd2[cmd.exe\nRunning in admin context];
    conhost[conhost.exe];
    cmd3[cmd.exe\nRunning in admin context];
    PSExec[PSExec.exe];
    PSExec2[PSExec.exe];
    ex --> cmd1;
    cmd1 --> ps1;
    ps1 --> cmd2;
    cmd2 --> cmd3;
    cmd2 --> conhost;
    cmd3 --> PSExec;
    cmd3 --> PSExec2;
</div>

## conhost.exe
And what about ```conhost.exe 0xffffffff -ForceV1```?
I did a bit of research about it and came to no intelligent conclusion whatsoever.
Hausec has a good [writeup](https://hausec.com/2021/07/26/cobalt-strike-and-tradecraft/) on cobalt strike which has
similar behaviour. I had a closer look into this and came across a post in
[strontic](https://strontic.github.io/xcyclopedia/library/conhost.exe-B577C5F724544F0C677F9C51D9B7B481.html) about this
topic which brought me to
[this](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cobaltstrike_process_patterns.yml)
Sigma rule.
On closer inspection of it, I can with high certainty say that this has nothing to do with Cobalt strike.

## Verdict
Now knowing the full path of what happened, I had another look into the "privilege escalation" aspect.
The logged-in user went from user to administrator, however as far as I was able to check via UAC, so all is in order.
This and the understanding of what was happening, made me feel certain enough that this is a false positive to get in
touch with the user.
The user was able to confirm that they are debugging some issues with the installed endpoint protection which fitted
into my view of the matter.

| Indicator                                  | Thoughts                                                | Verdict |
|--------------------------------------------|---------------------------------------------------------|---------|
| CMD started by User                        | Either compromise of host, or legitimate action by user | 50%     |
| Powershell started with Strange parameters | The parameters looks pretty malicious / suspicious      | 90%     |


**Verdict: False Positive**

## Next Steps

Get better processes, it's no good to use PSExec on a business device in my opinion
