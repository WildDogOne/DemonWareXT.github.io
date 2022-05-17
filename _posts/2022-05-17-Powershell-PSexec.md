---
title: Powershell and PSExec
date: 2022-05-17 21:39 +0200
categories: [Hunting, MDE]
tags: [mde, hunting, psexec]
---

```powershell
"cmd.exe" /c echo|set/p="C:\Temp\Tools"|powershell -NoP -W 1 -NonI -NoL "SaPs 'cmd' -Args '/c """cd /d',$([char]34+$Input+[char]34),'^&^& start /b cmd.exe"""' -Verb RunAs"
```
