## Steps to setup and execute the test automation framework on your machine:

1. git installation
Install git on your machine and clone the repo using following command:
git clone https://yieldwerxus.visualstudio.com/yieldWerx/_git/yieldWerx_Test_Automation

2. Install PyCharm IDE

3. Open the downloaded folder in PyCharm

4. Install Python using link:
https://www.python.org/downloads/

5. Set path for python in Environment Variables, the default installation path is typically:
 C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<version>.

6. CMD Commands to verify Python and pip installation:
python --version
(This should display the Python version number.)
pip --version
(This should display the pip version number.)

7. Open PyCharm Terminal and set path to your downloaded automation directory like:
PS D:\MyData\yieldWerx_Automation_1.0>

8. Enter following pip commands to install selenium and behave:
pip install selenium       (To install selenium)
pip show selenium          (To verify selenium installation)
pip install behave         (To install selenium)
pip show behave            (To verify selenium installation)

9. Steps to generate allure reports:
9.1 Install Java

9.2 Install Nodejs

9.3 Open windows powershell and type:
Get-ExecutionPolicy

9.4 Then type:
Set-ExecutionPolicy RemoteSigned           (powershell command to set the execution policy to remote signed)

9.5 npm install -g allure-commandline      (powershell command to install allure command line)

9.6 pip install allure-behave

9.7 allure –version                        (cmd command to check allure version)

9.8 behave -f allure_behave.formatter:AllureFormatter -o Reports/ features                                             (command to generate Reports folder containing json and csv files)

9.9 To see the allure reports in browser go to project path in terminal and execute command:
allure serve Reports
(if this command does not open the report in browser using PyCharm Terminal then try this command in cmd and remember to set the path to the project directory)

10. Commands to execute test cases without allure:
behave features                         (To run all the feature files inside features directory)

behave feature\login                    (To run specific feature files inside features sub directory)

behave feature\login\login.feature      (To run specific feature files inside features sub directory)


## Test Automation Framework folder & file structure:
"Allure Reports" folder contains files related to allure report

"Configurations" folder contains files having info like base url and creds

"features" folder contains all the feature files containing BDD scripts it also contains sub directories for each module of the yieldWerx web app.

"steps" folder contains steps definition files

"pages" folder contains page object files