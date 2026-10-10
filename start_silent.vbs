Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' Get the directory where this VBS file lives
Dim scriptDir
scriptDir = objFSO.GetParentFolderName(WScript.ScriptFullName)

' Run the tray server silently (no black window!)
objShell.Run "python """ & scriptDir & "\tray_server.py""", 0, False
