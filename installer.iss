[Setup]
; Имя приложения (отображается в установщике и в "Установка и удаление программ")
AppName=Calculator
AppVersion=1.0.0
AppPublisher=Sad_Scorpion
DefaultDirName={autopf}\Calculator
DefaultGroupName=Calculator
; Иконка в списке установленных программ — берём из самого exe
UninstallDisplayIcon={app}\Calculator.exe
; Куда сохранять готовый установщик
OutputDir=C:\Users\Sad_Scorpion\Desktop\git2\installer_output
OutputBaseFilename=Calculator_Setup
Compression=lzma2
SolidCompression=yes
; Современный мастер установки
WizardStyle=modern
; Архитектура: x64 (т.к. exe собран на 64-битной Windows)
ArchitecturesAllowed=x64
ArchitecturesInstallIn64BitMode=x64

[Languages]
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
; Галочка "Создать ярлык на рабочем столе"
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\Sad_Scorpion\Desktop\git2\dist\Calculator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Sad_Scorpion\Desktop\git2\myicon.ico"; DestDir: "{app}"; Flags: ignoreversion


[Icons]
; Ярлык в меню Пуск

Name: "{group}\Calculator"; Filename: "{app}\Calculator.exe"; IconFilename: "{app}\myicon.ico"
; Ярлык на рабочем столе
Name: "{autodesktop}\Calculator"; Filename: "{app}\Calculator.exe"; IconFilename: "{app}\myicon.ico"; Tasks: desktopicon

Name: "{group}\{cm:UninstallProgram,Calculator}"; Filename: "{uninstallexe}"

[Run]
; Предложить запустить калькулятор сразу после установки
Filename: "{app}\Calculator.exe"; Description: "{cm:LaunchProgram,Calculator}"; Flags: nowait postinstall skipifsilent