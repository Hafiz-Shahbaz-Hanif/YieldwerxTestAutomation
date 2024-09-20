Feature: SWM Rules

	@YWPD-TC-1207 @retry
	Scenario Outline: YWPD-TC-1207 - Verify that user is able to create & save SWM Bin Type Rules
		Given The user has successfully launched Web Application and logged in
		When Clicks on SWM Dropdown from the menu displayed on left side
		When Click on SWM Rules
		When Click "New SWM Rule" button from SWM Rules window
		When Enter a Rule Name and Description in the "General" tab
		When Select the "Input Data Selection" Tab
		When Select "<Source/Target Data Set Size>", "<Source/Target Probe>"
		When Then select "<Level>", "<Bin Type>", "<Rule Validation>"
		When Click on "Rule Definition" tab
		When After that select the "<Rule Type>", "<Bin Rule Detail>", "<Combine Wafer Bin>"
	    When Enter the "<Hard Bin Number / Name>", "<Soft Bin Number / Name>"
		When After that select "<Bin Flag / Other Fields Data>", "<Die Type>", "<Copy Parametric Data From>"
		When Click "Email Notification" tab
		When Enter valid "Owner Name", "Owner Email Address"
		When Enter "Additional emails" if needed
		When Click the "Save" button
		Then Verify that the rule has been saved successfully

	Examples:
		| Source/Target Data Set Size | Source/Target Probe | Level  | Bin Type | Rule Validation | Rule Type | Bin Rule Detail | Combine Wafer Bin | Hard Bin Number / Name | Soft Bin Number / Name | Bin Flag / Other Fields Data | Die Type     | Copy Parametric Data From |
		| Web Small Dataset           | 1M/1M               | Device | Hard Bin | All             | Bin Rule  |Both,Any,Any     | Custom BIN        | 30 / Rule 1H           | 30 / Rule 1S           | Fail, Source Wafer           | Probe Die(s) | None                      |


	@YWPD-TC-319 @retry
	Scenario Outline: YWPD-TC-319 - Verify that the user is able to create SWM Rule at Device Level and Rules
	Validation 'Custom', with web small dataset
	The objective of this test case is to ensure that the users can successfully create SWM Rule at Device Level and Rules Validation 'Custom', with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Rules
		When Click on "New SWM Rule" button from SWM Rules window
		When Create SWM Rules window will open and enter name as "<Name>" And description in "General" tab
		When Click the "Input Data Selection" tab and Select level as "<Level>", Rules Validation as "<Rules Validation>"
		When Select the Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select the source device as "<Source Device>" and source probe as (1|M)
		When Select Target Facility  as "<Target Facility>", Target Work Center  as "<Target Work Center>
		When Select Target Probe as (1|M) and Target Device as "<Target Device>"
		When Click "Rule Definition" tab And Select rule Type from "<Select Rule Type>" drop down
		When Select one option from Die Exist in Wafers as "<Die Exist in Wafers>"
		When Select Source Wafer Bin as
			| Source Bin   |
			| <Source Bin> |
		When Select Target Wafer Bin as
			| Target Bin   |
			| <Target Bin> |
		When Select "Combine Bin" option from Combine Wafer Bin Details as "<Combine Wafer Bin Details>"
		When Provide Hard Bin Number as "<Hard Bin Number>", Soft Bin Number as "<Soft Bin Number>"
		When Select Bin Flag and other fields data
		When Select Die Type as "<Die Type>"
		When Select the one option from "<Copy Parametric Data (PTR,FTR & MPR) From>"
		When Enable "Copy bin number, probe site, reticle site and die type data as parameters?" checkbox if needed
		When Click "Email Notification" tab
		When Enter valid "Owner Name", "Owner Email Address" And Enter additional emails if needed
		When Click the "Save" button
		Then Verify that the rule will be saved and appear in the SWM Rules window
		"""
		SWMRules table in database, and email will be sent at your given email (s)
		"""

	Examples:
		| Name                              | Level  | Rules Validation | Source Facility   | Source Work Center | Source Device | Target Facility   | Target Work Center | Target Device | Select Rule Type | Die Exist in Wafers                        | Combine Wafer Bin Details | Hard Bin Number | Soft Bin Number | Die Type     | Copy Parametric Data (PTR,FTR & MPR) From | Source Bin   | Target Bin  |
		| 4670-PrePostMerge-P-P             | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | Both                                      | Passing      | Passing     |
		| 4670-PrePostMerge-P-F             | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | Both                                      | Passing      | Failing     |
		| 4670-PrePostMerge-F-P             | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Source Wafer BIN          | NA              | NA              | NA           | Both                                      | Failing      | Passing     |
		| 4670-PrePostMerge-F-F             | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | Both                                      | Failing      | Failing     |
		| 4670-PrePostMerge-Missing-Missing | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | None                                      | Missing      | Missing     |
		| 4670-PrePostMerge-P-Missing       | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Custom BIN                | 61              | 61              | Probe Die(s) | Both                                      | Missing      | Passing     |
		| 4670-PrePostMerge-Missing-P       | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Custom BIN                | 60              | 60              | Probe Die(s) | Both                                      | Passing      | Missing     |
		| 4670-PrePostMerge-F-Missing       | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Source Wafer BIN          | NA              | NA              | NA           | Both                                      | Missing      | Failing     |
		| 4670-PrePostMerge-Missing-F       | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA           | Both                                      | Failing      | Missing     |
		| 4670-PrePostMerge-P-NA            | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Only Source Wafer             | Custom BIN                | 61              | 61              | Probe Die(s) | Source Wafer                              |              | Passing     |
		| 4670-PrePostMerge-F-NA            | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Only Source Wafer             | Source Wafer BIN          | NA              | NA              | NA           | Source Wafer                              |              | Failing     |
		| 4670-PrePostMerge-NA-P            | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Only Target Wafer             | Custom BIN                | 60              | 60              | Probe Die(s) | Target Wafer                              | Passing      |             |
		| 4670-PrePostMerge-NA-F            | Device | Custom           | WEB SMALL DATASET | WAFER SORT         | 4670          | WEB SMALL DATASET | WAFER SORT         | 4670          | BIN Rule         | Die Exist in Only Target Wafer             | Target Wafer BIN          | NA              | NA              | NA           | Target Wafer                              | Failing      |             |


	@YWPD-TC-307 @retry
	Scenario Outline: YWPD-TC-307 - Verify that the user is able to create Test Program Level SWM Rule with Web Small
	Dataset
	The objective of this test case is to ensure that the users can successfully create Test Program Level SWM Rule with Web Small Dataset
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Rules
		When Click on "New SWM Rule" button from SWM Rules window
		When Create SWM Rules window will open so enter name as "<Name>" And description in "General" tab
		When Click "Input Data Selection" And Select level as "<Level>"
		When Select the Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select Source Device as "<Source Device>"
		When Select Source Probe as "(1|M)" and Source Test Program as "<Source Test Program>"
		When Select Target Facility  as "<Target Facility>", Target Work Center  as "<Target Work Center>
		When Select Target Device as "<Target Device>"
		When Select Target Test Program as "<Target Test Program>", Target Probe "(1|M)"
		When Click the tab "Rule Definition" and Select rule Type from "<Select Rule Type>" drop down
		When Select the Die Exist in Wafers as "<Die Exist in Wafers>"
		When Select Source Wafer Bin as "<Source Bin>"
		When Select Target Wafer Bin as "<Target Bin>"
		When Select Combine Wafer Bin Details as "<Combine Wafer Bin Details>"
		When Give Hard Bin Number as "<Hard Bin Number>", Soft Bin Number as "<Soft Bin Number>"
		When Select the Bin Flag and the other fields data
		When Select the Die Type "<Die Type>"
		When Select from "<Copy Parametric Data (PTR,FTR & MPR) From>"
		When Enable the following checkbox if required
        """
        "Copy bin number, probe site, reticle site and die type data as parameters?" checkbox
        """
		When Click "Email Notification" tab
		When Enter the valid "Owner Name", "Owner Email Address" and the Enter additional emails if needed
		When Click the "Save" button
		Then Verify that the test program level rule will be saved and appear in the SWM Rules window
		"""
		SWMRules table in database, and email will be sent at your given email (s)
		"""

	Examples:
		| Name                                | Level        | Rules Validation | Source Facility   | Source Work Center | Source Device | Source Test Program | Target Facility   | Target Work Center | Target Device | Target Test Program | Select Rule Type | Die Exist in Wafers                        | Combine Wafer Bin Details | Hard Bin Number | Soft Bin Number | Die Type | Copy Parametric Data (PTR,FTR & MPR) From | Source Bin   | Target Bin  |
		| 4670-PrePostMerge-P-P _TestProgram  | Test Program | N/A              | WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA       | Both                                      | Passing      | Passing     |
		| 4670-PrePostMerge-F-F - TestProgram | Test Program | N/A              | WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA       | Both                                      | Failing      | Failing     |
		| 4670-PrePostMerge-P-F - TestProgram | Test Program | N/A              | WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | BIN Rule         | Die Exist in Both Source and Target Wafers | Target Wafer BIN          | NA              | NA              | NA       | Both                                      | Passing      | Failing     |
		| 4670-PrePostMerge-F-P - TestProgram | Test Program | N/A              | WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | BIN Rule         | Die Exist in Both Source and Target Wafers | Source Wafer BIN          | NA              | NA              | NA       | Both                                      | Failing      | Passing     |


	@YWPD-TC-325 @retry
	Scenario: YWPD-TC-325 - Verify that the user is able to Modify SWM Rule successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully Modify SWM Rule with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Rules
		When See the list of already created SWM rules
		When Click "Edit" button available for each rule
		When Make changes that you want
		When Change Source Facility, Source Work Center
		When Change Source Device, Source test Program, Source Probe
		When Change Target Facility, Target Work Center
		When Change Target Device, Target test Program, Target Probe
		When Click "Rule Definition" tab And Change rule Type from "<Select Rule Type>" drop down
		When Change "Bin Rule Details" combinations for "Die Exist in Both Source and Target Wafers"
		When Change "Combine Bin" option from "Combine Wafer Bin Details" tab
		When Change "Hard Bin Number" and "Soft Bin Number" details
		When Change Bin Flag and other fields data
		When Change "Die Type" like "Probe Die(s)" from available Die Type options
		When Change any option in Copy Parametric Data (PTR, FTR, and MPR)
		When Enable or Disable the checkbox
		"""
		"Copy bin number, probe site, reticle site and die type data as parameters?" checkbox if
		needed
		"""
		When Click "Email Notification" tab
		When Change valid "Owner Name", "Owner Email Address" And Change additional emails if needed
		When Click the "Save" button
		Then Verify that the edited rule will be saved and appear in the SWM Rules window


	@YWPD-TC-327 @retry
	Scenario: YWPD-TC-327- Verify that the user is able to Copy SWM Rule with web small dataset
	The objective of this test case is to ensure that the users can successfully Copy SWM Rule with web small dataset
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Rules
		When See the list of already created SWM rules
		When Click Copy button available infront of each already created rule
		When Create SWM Rule window of already created SWM rule will open
		When Change name and description from General tab
		When Change Source Facility, Source Work Center
		When Change Source Device, Source test Program, Source Probe
		When Change Target Facility, Target Work Center
		When Change Target Device, Target test Program, Target Probe
		When Click "Rule Definition" tab And Change rule Type from "<Select Rule Type>" drop down
		When Change "Bin Rule Details" combinations for "Die Exist in Both Source and Target Wafers"
		When Change "Combine Bin" option from "Combine Wafer Bin Details" tab
		When Change "Hard Bin Number" and "Soft Bin Number" details
		When Change Bin Flag and other fields data
		When Change "Die Type" like "Probe Die(s)" from available Die Type options
		When Change any option in Copy Parametric Data (PTR, FTR, and MPR)
		When Enable or Disable the checkbox
		"""
		"Copy bin number, probe site, reticle site and die type data as parameters?" checkbox if
		needed
		"""
		When Click "Email Notification" tab
		When Change valid "Owner Name", "Owner Email Address" And Change additional emails if needed
		When Click the "Save" button
		Then Verify that the copied rule will be saved
		"""
		and appear in the SWM Rules window, SWMRules table in database,
		and email will be sent at your given email (s)
		"""


	@YWPD-TC-326 @retry
	Scenario: YWPD-TC-326 - Verify that the user is able to delete SWM Rule successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully delete SWM Rule related to web small dataset
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Rules
		When See the list of already created SWM rules
		When Click "Delete" button available at the end of each rule
		When Confirmation Required pop-up window will appear with "Yes" and "No" buttons
		When Click "Yes" to delete the SWM rule
		Then Verify that the rule will be deleted
		"""
		and window will be refresh and rule will be deleted from Web User Interface and from SWMRules table in database as well
		"""