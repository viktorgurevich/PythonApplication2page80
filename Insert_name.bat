
@echo off 
REM CD C:\Projects\PythonApplication2page80
REM https://simply-python.com/2014/03/20/easy-invoke-pip-install-using-batch-commands/
REM Batch command to easily invoke the pip install/ uninstall function.
REM User can quickly install the required python module by just entering the module name
REM Runs on Windows
REM C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\    --VG: find via path command 
:start
REM The syntax of the command is incorrect.???? which one???
REM cls
set %scriptPath%=C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Scripts\
REM echo %scriptPath%

echo Select menu
echo ======================================================================================
echo 1. Display python modules being installed using pip function
echo 2. Pip installation (individual files)
echo 3. Pip uninstall
echo.
 
set /p x=Pick:
IF '%x%' == '1' GOTO NUM_1
IF '%x%' == '2' GOTO NUM_2
IF '%x%' == '3' GOTO NUM_3
GOTO start
 
:NUM_1

cd %scriptPath%
pip freeze
pause
exit
 
:NUM_2
echo  Enter a filename to start install using pip
set INPUT=
set /P INPUT=Type input:%=%
 
cd \
cd %scriptPath%
pip install %INPUT%
 
pause
exit
 
:NUM_3
echo  Enter a filename to UNINSTALL using pip
set INPUT=
set /P INPUT=Type input:%=%
 
cd \
cd %scriptPath%
pip uninstall %INPUT%
 
pause
REM exit C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Lib\ensurepip\_bundled