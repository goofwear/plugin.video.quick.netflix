#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%
#SingleInstance force

^+s::
SendInput !{F4}
ExitApp

#IfWinActive ahk_class Chrome_WidgetWin_1

Enter::
SendInput, p
return

^d::
SendInput, {Enter}
return

^b::
SendInput {Home}
return

^f::
SendInput {End}   
return

^p::
SendInput, {space}
return

^+b::
SendInput ^w
return
