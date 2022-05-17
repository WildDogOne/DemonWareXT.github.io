---
title: Powershell and PSExec
date: 2022-05-17 21:39 +0200
categories: [Hunting, MDE]
tags: [mde, hunting, psexec]
---

Today we investigate some strange behaviour from a possibly user executed Powershell session.
Everything started with an explorer.exe running the following comandline

```powershell
"cmd.exe" /c echo|set/p="C:\Temp\Tools"|powershell -NoP -W 1 -NonI -NoL "SaPs 'cmd' -Args '/c """cd /d',$([char]34+$Input+[char]34),'^&^& start /b cmd.exe"""' -Verb RunAs"
```

On further inspection, this commandline seems to switch the execution path to C:\Temp\Tools and elevate to administrative rights.
A good indicator in my opinion, are the flags of a powershell execution:
 * -NoP -> -NoProfile, who would do that?
 * -W 1 -> Window 1, never seen this one before
 * -NonI -> NonInteractive
 * -NoL
