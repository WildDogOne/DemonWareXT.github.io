---
title: Powershell and PSExec
date: 2022-05-17 21:39 +0200
categories: [Hunting, MDE]
tags: [mde, hunting, psexec]
---
{% include mermaid.liquid %}

Today we investigate some strange behaviour from a (possibly user) executed Powershell session.

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

Whe "-W 1" param is definitelly fancy for me, usually one would expect -W Hidden, but it seems like -W 1 accomplishes
the same job.


<div class="mermaid">
flowchart LR;
    ex[explorer.exe\nRunning in user context];
    cmd1[cmd.exe\nRunning in user context];
    ps1[powershell.exe\nRunning in user context];
    cmd2[cmd.exe\nRunning in admin context];
    ex --> cmd1;
    cmd1 --> ps1;
    ps1 --> cmd2;
</div>
