Feature: AMG Policies

	@YWPD-TC-913 @retry
	Scenario Outline: YWPD-TC-913 - Verify that user is able to successfully generate the Assembly Map Test Program Level Policy
	The objective of this test case is to ensure that users can successfully Create Assembly Map Test Program Level Policy with Small Data Set favorite selection. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide the assembly map policy "<Name>" in the "General" tab
		And Navigate into the "Parameter" tab and select the "<Data Set Size>", and "<Facility>"
		And After selecting facility data will be populated automatically for work center, device and test program
		And Choose wafer from "<Generate Assembly Map From>" dropdown available on the parameters tab
		And Navigate into the "Generation" tab
		And Choose the AMG format from "<Conversion of Assembly Map File to Format>" dropdown
		And Navigate into the "Output" tab
		And Enter the folder path into the "<Main Directory>" Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the "<File Name Format>" into the input field, Enter @ in the input field, options list will be visible select option from the list
		And Choose the "<Output Path>" from the available Options
		And Click on the "Add Path" button
		And Check on the "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved AMG policy is shown in the AMG Policies grid section
		And Enable your saved policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		And A wafer will be saved into the desktop application
#		And Open desktop application
#		And Click the Wafer Map Report icon
#		And Select the <Data Set Size> and A wafer and execute report
#		Then Verify the < Expected A Wafer>, <Expected A Wafer Legend> with wafer ID 1 and <Expected A Wafer File> will also be saved into the given path

	Examples:
		| Data Set Size    | Name                      | Facility            | Generate Assembly Map From              | Conversion of Assembly Map File to Format | Main Directory | If Previous Assembly Map File Exists | File Name Format          | Output Path         | Save Assembly Map as Wafer | Expected A Wafer       | Expected A Wafer Legend      | Expected A Wafer File      |
		|  Small Data Set  | Test Program Level Policy | WEB SMALL DATA SET  | Pre PAT Final Probe (Probe Pass 1 OR M) | ASCII TMA                                 | D:\AMG         | Rename Old and Create New            | @FacilityID, @Date, @Time | Local/Network Drive | Enable                     | AMG_SD_TPLP_AWafer.png | AMG_SD_TPLP_AWaferLegend.png | AMG_SD_TPLP_AWaferFile.tma |


	@YWPD-TC-914 @retry
	Scenario Outline: YWPD-TC-914 - Verify that user is able to successfully generate the Assembly Map Device Level Policy
	The objective of this test case is to ensure that users can successfully Create Assembly Map Device Level Policy with Small Data Set favorite selection. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide the assembly map device level policy "<Name>" in the General tab
		And Navigate into the "Parameter" tab and select the "<Data Set Size>", and "<Facility>"
		And After selecting facility data will be populated automatically for work center, device and test program
		And Enable "<Apply AMG Policy to Device Level>" check box
		And Choose wafer from "<Generate Assembly Map From>" dropdown available on the parameters tab
		And Navigate into the "Generation" tab
		And Choose the AMG format from "<Conversion of Assembly Map File to Format>" dropdown
		And Navigate into the "Output" tab
		And Enter the folder path into the "<Main Directory>" Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the "<File Name Format>" into the input field, Enter @ in the input field, options list will be visible select option from the list
		And Choose the "<Output Path>" from the available Options
		And Click on the "Add Path" button
		And Check on the "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved AMG Device Level policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		And A wafer will be saved into the desktop application in <Data Set Size>
#		And Open desktop application
#		And Click the Wafer Map Report icon
#		And Select the <Data Set Size> and A wafer and execute report
#		Then Verify the <Expected A Wafer>, <Expected A Wafer Legend> with wafer ID 1, and <Expected A Wafer File> will also be saved into the given path

	Examples:
		| Data Set Size    | Name                | Facility            | Apply AMG Policy to Device Level | Generate Assembly Map From              | Conversion of Assembly Map File to Format | Main Directory | If Previous Assembly Map File Exists | File Name Format          | Output Path         | Save Assembly Map as Wafer | Expected A Wafer      | Expected A Wafer Legend     | Expected A Wafer File     |
		|  Small Data Set  | Device Level Policy | WEB SMALL DATA SET  | Enable                           | Pre PAT Final Probe (Probe Pass 1 OR M) | ASCII TMA                                 | D:\AMG         | Rename Old and Create New            | @FacilityID, @Date, @Time | Local/Network Drive | Enable                     | AMG_SD_DLP_AWafer.png | AMG_SD_DLP_AWaferLegend.png | AMG_SD_DLP_AWaferFile.tma |


	@YWPD-TC-915 @retry
	Scenario: YWPD-TC-915 - Verify that user is able to successfully generate the Assembly Map for Lot Completion
	The objective of this test case is to ensure that users can successfully Create Assembly Map for Lot Completion. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide assembly map policy name as "AMG Device Level Policy for Lot Completion" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Enable "Apply AMG Policy To Device Level" check box or proceed without enabling this check box for test program level
		And Enable "Check for Lot Completion" checkbox
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the AMG format from "Conversion of Assembly Map File to Format" dropdown from the following list
			"""
			(ASCII TMA, ASCII TXT, Format3,Format4,ATX Format, Wafer Map Format (A-PM-90A/UF Series),
			Laurier, SINF(3 Digit), ASE Format, SINF (2 Digit) , ASCII NAM, ASCII TMA 2, SINF 2 Digit Diode,
			ASCII NAM 2, ASCII, TXT 2 ,SINF (3 Digit) 2)
			"""
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully


#		Following steps are related to desktop app that is why these cannot be automated
#		Then Verify that A wafer is saved into the desktop application and policy will also be saved into the 'AssemblyMapPolicy' table in database
#		Then Verify that the AMG File is also saved into the given path


	@YWPD-TC-916 @retry
	Scenario: YWPD-TC-916 - Verify that user is able to successfully generate the Assembly Map for SBL/SYL Integration
	The objective of this test case is to ensure that users can successfully Create Assembly Map for SBL/SYL Integration. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide policy name as "AMG Device Level Policy for SBL/SYL Integration" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Enable "Apply AMG Policy To Device Level" check box or proceed without enabling this check box for test program level
		And Enable "Enable SBL/SYL Integration" checkbox
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the AMG format from "Conversion of Assembly Map File to Format" dropdown from the following list
			"""
			(ASCII TMA, ASCII TXT, Format3,Format4,ATX Format, Wafer Map Format (A-PM-90A/UF Series),
			Laurier, SINF(3 Digit), ASE Format, SINF (2 Digit) , ASCII NAM, ASCII TMA 2, SINF 2 Digit Diode,
			ASCII NAM 2, ASCII, TXT 2 ,SINF (3 Digit) 2)
			"""
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved SBL/SYL policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully


#		Following steps are related to desktop app that is why these cannot be automated
#		Then Verify that A wafer is saved into the desktop application and policy will also be saved into the 'AssemblyMapPolicy' table in database
#		Then Verify that the AMG File is also saved into the given path


	@YWPD-TC-923 @retry
	Scenario: YWPD-TC-923 - Verify that user is able to Un-Automate the AMG policy
	The objective of this test case is to ensure that users can successfully Un-Automate the AMG policy
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide policy name as "AMG Device Level Policy for SBL/SYL Integration" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Enable "Apply AMG Policy To Device Level" check box or proceed without enabling this check box for test program level
		And Enable "Enable SBL/SYL Integration" checkbox
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the AMG format from "Conversion of Assembly Map File to Format" dropdown from the following list
			"""
			(ASCII TMA, ASCII TXT, Format3,Format4,ATX Format, Wafer Map Format (A-PM-90A/UF Series),
			Laurier, SINF(3 Digit), ASE Format, SINF (2 Digit) , ASCII NAM, ASCII TMA 2, SINF 2 Digit Diode,
			ASCII NAM 2, ASCII, TXT 2 ,SINF (3 Digit) 2)
			"""
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved SBL/SYL policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		And The AMG Policy will be successfully activated
		And A wafer will be saved into the desktop application and policy will also be saved into the "AssemblyMapPolicy" table in database
		And File will also be saved into the given path
		And Disable the check box that is available in front of each policy
		And Confirmation pop-up will appear with the written text message "Are you sure you want to un-automate this policy"
		And Verify that when user clicks "YES", Page will be refreshed and popup stating "Policy status is updated successfully" will appear
		Then Verify that On the Assembly Map Policy window check box will be disabled and policy is un-automated


	@YWPD-TC-924 @retry
	Scenario: YWPD-TC-924 - Verify that user is able to successfully update the Assembly Map Policy with the new version
	The objective of this test case is to ensure that users can successfully update the Assembly Map Policy with the new version
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Create New Assembly Map Policy as a Pre-Requisite
		And You will see the list of created AMG polices in "Assembly Map Policies" grid section
		And Disable or Un-automate the policy that you want to update
		And Click the "Edit" icon against any policy that you want to update
		And Create assembly map policy window will open now you can make changes of your choice in the policy
		And Click on the save button available at the end
		And Save changes pop-up will appear with message as "You are attempting to save changes to an existing policy, would you like to save these changes under the existing version number or create a new one?"
		And Check the "Save to a new version number option"
		And Enter the new version like "2.0"
		And Click on OK button
		And Confirmation pop-up will appear, a message written on the box is "Are you sure you want to mark the policy version '2.0' as active policy version?"
		And Click on "Yes"
		And "Successful automated policy has been saved" message will appear and page will be refresh
		Then Verify that a New entry of the updated policy with new version is added in the Assembly Map Policy grid section as an active policy


	@YWPD-TC-925 @retry
	Scenario: YWPD-TC-925 - Verify that user is able to successfully update the Assembly Map Policy with the existing version
	The objective of this test case is to ensure that users can successfully update the Assembly Map Policy with the existing version
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Create New Assembly Map Policy as a Pre-Requisite
		And You will see the list of created AMG polices in "Assembly Map Policies" grid section
		And Disable or Un-automate the policy that you want to update
		And Click the "Edit" icon against any policy that you want to update
		And Create assembly map policy window will open now where you can make changes of your choice in the policy
		And Click on the save button available at the end
		And Save changes pop-up will appear with message as "You are attempting to save changes to an existing policy, would you like to save these changes under the existing version number or create a new one?"
		And Select "Keep Existing version number" option
		And Click on OK button
		And "Successful automated policy has been saved" message will appear and page will be refresh
		Then Verify that a new entry of the updated policy with existing version is added in the Assembly Map Policy grid section as an active policy


	@YWPD-TC-927 @retry
	Scenario: YWPD-TC-927 - Verify that the user is able to Archive an AMG policy successfully
	The objective of this test case is to ensure that users can successfully Archive an AMG policy successfully
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Create New Assembly Map Policy as a Pre-Requisite
		And You will see the list of created AMG polices in "Assembly Map Policies" grid section
		And Click on the delete icon of AMG policy available at the end of each created policy
		And "Assembly Map Policy delete confirmation" popup appears
		And Number of wafers with status and count grid are shown on the confirmation popup window
		And Click on the "Archive" button from the "Assembly Map Policy delete confirmation" popup
		Then Verify that the Policy is Archived successfully


	@YWPD-TC-926 @retry
	Scenario: YWPD-TC-926 - Verify that user is able to Delete an AMG policy successfully
	The objective of this test case is to ensure that users can successfully Delete an AMG policy successfully
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Create New Assembly Map Policy as a Pre-Requisite
		And You will see the list of created AMG polices in "Assembly Map Policies" grid section
		And Click on the delete icon of AMG policy available at the end of each created policy
		And "Assembly Map Policy delete confirmation" popup appears
		And Number of wafers with status and count grid are shown on the confirmation popup window
		And Select the delete button
		And Click on continue button
		Then Verify that the AMG policy is deleted successfully

	@YWPD-TC-2898 @retry
	Scenario: YWPD-TC-2898 - Verify that user is able to successfully generate the Assembly Map with 'Standard Rule file'
	The objective of this test case is to ensure that users can successfully Create Assembly Map with 'Standard Rule file'. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide assembly map policy name as "AMG Device Level Policy for MES Integration" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Enable "Apply AMG Policy To Device Level" check box or proceed without enabling this check box for test program level
		And Enable the checkbox "Turn on MES Integration"
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the "G85 XML" format from "Conversion of Assembly Map File to Format"
		And After selecting AMG format from the above list Die bin details box will appear below in the "Generation" tab
		And Add the path location of the standard rule file in the "File Directory" input field
		And Add the file extension name without a dot on the input field of "File Extension"
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		And Verify that the A wafer is saved in the desktop application against the selected data
#		And Verify that the AMG wafer file is saved into the given path


	@YWPD-TC-920 @retry
	Scenario: YWPD-TC-920 - Verify that user is able to successfully generate the Assembly Map with 'Standard Rule file'
	The objective of this test case is to ensure that users can successfully Create  Assembly Map with 'Standard Rule file'. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide assembly map policy name as "AMG Device Level Policy for MES Integration" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Enable "Apply AMG Policy To Device Level" check box or proceed without enabling this check box for test program level
		And Enable the checkbox "Turn on MES Integration"
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the "SINF (3 Digit) 2" format from "Conversion of Assembly Map File to Format"
		And After selecting AMG format from the above list Die bin details box will appear below the "Generation" tab
		And Enable "Die Type" and select die type from the drop-down list
		And Enable "Bin definition" and add Hard Bin/Soft Bin number in the input field
		And Enable "Pass/Fail Bin Flag" and select the pass/fail flag from the drop-down list
		And Enter Die Character in the input field user can add a maximum of 3 characters
		And After selecting/adding complete die bin details click on the "Add Die/Bin Detail" button
		And All the Die/Bin details will be added in the "Saved Die/Bin Details" section
		And Enable "Merge Assembly Map with Device Map"
		And Add the path location of the standard rule file in the "File Directory" input field
		And Add the file extension name without a dot on the input field of "File Extension"
		And Make sure that standard rule file name and device name are same
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		And Verify that the A wafer is saved in the desktop application against the selected data
#		And Verify that the AMG wafer file is saved into the given path


	@YWPD-TC-919 @retry
	Scenario: YWPD-TC-919 - Verify that user is able to successfully generate the Assembly Map with Die/Bin Details for a test program level policy
	The objective of this test case is to ensure that users can successfully Create Assembly Map with Die/Bin Details for a test program level policy. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide assembly map policy name as "AMG Test Program Level Policy with Die/Bin Details" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the "SINF (3 Digit) 2" format from "Conversion of Assembly Map File to Format"
		And After selecting AMG format from the above list Die bin details box will appear below the "Generation" tab
		And Enable "Die Type" and select die type from the drop-down list
		And Enable "Bin definition" and add Hard Bin/Soft Bin number in the input field
		And Enable "Pass/Fail Bin Flag" and select the pass/fail flag from the drop-down list
		And Enter Die Character in the input field user can add a maximum of 3 characters
		And After selecting/adding complete die bin details click on the "Add Die/Bin Detail" button
		And All the Die/Bin details will be added in the "Saved Die/Bin Details" section
		And Enable "Merge Assembly Map with Device Map"
		And Add the path location of the standard rule file in the "File Directory" input field
		And Add the file extension name without a dot on the input field of "File Extension"
		And Make sure that standard rule file name and device name are same
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		And Verify that the A wafer is saved in the desktop application against the selected data
#		And Verify that the AMG wafer file is saved into the given path


	@YWPD-TC-918 @retry
	Scenario: YWPD-TC-918 - Verify that user is able to successfully generate the Assembly Map with Die/Bin Details for a device level policy
	The objective of this test case is to ensure that users can successfully Create Assembly Map with Die/Bin Details for a device level policy. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide assembly map policy name as "AMG Device Level Policy with Die/Bin Details" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Enable "Apply AMG Policy To Device Level" check box or proceed without enabling this check box for test program level
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the "SINF (3 Digit) 2" format from "Conversion of Assembly Map File to Format"
		And After selecting AMG format from the above list Die bin details box will appear below the "Generation" tab
		And Enable "Die Type" and select die type from the drop-down list
		And Enable "Bin definition" and add Hard Bin/Soft Bin number in the input field
		And Enable "Pass/Fail Bin Flag" and select the pass/fail flag from the drop-down list
		And Enter Die Character in the input field user can add a maximum of 3 characters
		And After selecting/adding complete die bin details click on the "Add Die/Bin Detail" button
		And All the Die/Bin details will be added in the "Saved Die/Bin Details" section
		And Enable "Merge Assembly Map with Device Map"
		And Add the path location of the standard rule file in the "File Directory" input field
		And Add the file extension name without a dot on the input field of "File Extension"
		And Make sure that standard rule file name and device name are same
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		And Verify that the A wafer is saved in the desktop application against the selected data
#		And Verify that the AMG wafer file is saved into the given path


	@YWPD-TC-917 @retry
	Scenario: YWPD-TC-917 - Verify that user is able to successfully generate the Assembly Map with 'Standard Rule file'
	The objective of this test case is to ensure that users can successfully Create  Assembly Map with 'Standard Rule file'. Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide assembly map policy name as "AMG Device Level Policy for MES Integration" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Enable "Apply AMG Policy To Device Level" check box or proceed without enabling this check box for test program level
		And Enable the checkbox "Turn on MES Integration"
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the AMG format from "Conversion of Assembly Map File to Format" dropdown from the following list
			"""
			(ASCII TMA, ASCII TXT, Format3,Format4,ATX Format, Wafer Map Format (A-PM-90A/UF Series),
			Laurier, SINF(3 Digit), ASE Format, SINF (2 Digit) , ASCII NAM, ASCII TMA 2, SINF 2 Digit Diode,
			ASCII NAM 2, ASCII, TXT 2 ,SINF (3 Digit) 2)
			"""
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Enable the check box of "<Save Assembly Map as Wafer>"
		And Click on the save button available at the end
		And Saved policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		And Verify that the A wafer is saved in the desktop application against the selected data
#		And Verify that the AMG wafer file is saved into the given path


	@YWPD-TC-922 @retry
	Scenario: YWPD-TC-922 - Verify that user is able to successfully generate the Assembly Map without selecting the option "Save assembly map as a wafer" for test program level
	The objective of this test case is to ensure that users can successfully Create Assembly Map  without selecting the option " Save assembly map as a wafer". Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide assembly map policy name as "AMG Test Program Level Policy" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the AMG format from "Conversion of Assembly Map File to Format" dropdown from the following list
			"""
			(ASCII TMA, ASCII TXT, Format3,Format4,ATX Format, Wafer Map Format (A-PM-90A/UF Series),
			Laurier, SINF(3 Digit), ASE Format, SINF (2 Digit) , ASCII NAM, ASCII TMA 2, SINF 2 Digit Diode,
			ASCII NAM 2, ASCII, TXT 2 ,SINF (3 Digit) 2)
			"""
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Click on the save button available at the end
		And Saved policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		Then Verify that the A wafer is not saved into the desktop application and policy will be saved into the 'AssemblyMapPolicy' table in database
#		Then Verify that the AMG wafer File will be saved into the given path



	@YWPD-TC-921 @retry
	Scenario: YWPD-TC-921 - Verify that user is able to successfully generate the Assembly Map without selecting the option "Save assembly map as a wafer" for test program level
	The objective of this test case is to ensure that users can successfully Create Assembly Map  without selecting the option " Save assembly map as a wafer". Additionally, this test case aims to validate the functionality of Assembly Map Policies and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Click on the Create Assembly Map Policy button
		And Provide assembly map policy name as "AMG Device Level Policy" in "General" tab
		And Navigate into "Parameter" tab and select the data facility
		And After selecting facility data will be populated automatically for work center, device and test program, for device level test program will be gray out
		And Enable the "Apply AMG Policy To Device Level" check box
		And Choose the wafer for creating AMG policy from the following options from the
			"""
			"Generate Assembly Map From" dropdown, available in parameters tab options are:
			(Pre PAT Final Probe (Probe Pass 1 OR M)),Auto-Generated, Combine Wafer (C ),
			PAT Wafer (P), MVPAT Wafer (V), GDBN Wafer (G), GDBN-Z Wafer (Z), Manual Generated: Combine Wafer (MC ),
			PAT Wafer (MP), MVPAT Wafer (MV), GDBN, Wafer (MG), GDBN-Z Wafer (MZ) )
			"""
		And Navigate into the "Generation" tab
		And Choose the AMG format from "Conversion of Assembly Map File to Format" dropdown from the following list
			"""
			(ASCII TMA, ASCII TXT, Format3,Format4,ATX Format, Wafer Map Format (A-PM-90A/UF Series),
			Laurier, SINF(3 Digit), ASE Format, SINF (2 Digit) , ASCII NAM, ASCII TMA 2, SINF 2 Digit Diode,
			ASCII NAM 2, ASCII, TXT 2 ,SINF (3 Digit) 2)
			"""
		And Navigate into the "Output" tab
		And Enter the "Main Directory" folder path into the Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" that path has been added
		And Click on the save button available at the end
		And Saved policy is shown in the AMG Policies grid section
		And Enable your saved Device Level AMG policy
		Then Policy will be activated successfully

#		Following steps are related to desktop app that is why these cannot be automated
#		Then Verify that the A wafer is not saved into the desktop application and policy will be saved into the 'AssemblyMapPolicy' table in database
#		Then Verify that the AMG wafer File will be saved into the given path



	@YWPD-TC-940 @retry
	Scenario: YWPD-TC-940 - Verify that user is able to successfully generate the Assembly Map, policies, generations and requests with active wafers
	AMG
		Given The user successfully opened the yieldWerx web application and login
		When Open Assembly Map Policies module
		And Create New Assembly Map Policy as a Pre-Requisite
		And Navigate to "Assembly Map Generations" module
		And Assembly Map generations module have two sections, "Assembly Map Policies" and "Generations" section
		Then Verify that Assembly map policies section contain all the active processed policies list
		And Verify that Grid contains Name, version, type, facility, work center, device, test program, date modified, successful, failed and pending columns are available



	@YWPD-TC-939 @retry
	Scenario: YWPD-TC-939 - Verify that user is able to Reset  Manual Assembly/Pick Map data Selection
	The objective of this test case is to ensure that users can successfully Reset  Manual Assembly/Pick Map data Selection
		Given The user successfully opened the yieldWerx web application and login
		When Open Generate Manual Assembly/Pick Map
		And Select facility data to generate Manual Assembly/Pick Map
		And After selecting the data facility, Work Center, Device, Test Program, Lot, and wafers should be selected automatically
		And Click on the Reset Button
		Then Verify that All the data selections are reset



	@YWPD-TC-936 @retry
	Scenario: YWPD-TC-936 - Verify that user is able to Generate a Manual Assembly/Pick Map with die bin details
	AMG
		Given The user successfully opened the yieldWerx web application and login
		When Open Generate Manual Assembly/Pick Map
		And Select the facility data
		And After selecting the facility, work center, device, test program, lot and wafer will be selected automatically
		And Select the Wafer plotting option as "Actual Wafer/Die Size Settings"
		And Click on the Plot Wafer Map to Pick Map Die(S)
		And User will be redirected to the Bin Wafer Map screen
		And Select the few wafers die
		And Click on the plus sign available at the end on right side and expand the options
		And Select mark as assemble from the option
		And "Selected dies have been marked as assembled" message will appear and selected dies will be marked
		And Again click on the plus sign available at the end on the right side and expand the options
		And Click on the "Save and generate AMG"
		And User will be redirected to "Generations" tab
		And Choose the "ASCII TXT" format from "Conversion of Assembly Map File to Format"
		And After selecting AMG format from the above list Die bin details box will appear below the "Generation" tab
		And Enable "Die Type" and select die type from the drop-down list
		And Enable "Bin definition" and add Hard Bin/Soft Bin number in the input field
		And Enable "Pass/Fail Bin Flag" and select the pass/fail flag from the drop-down list
		And Enter Die Character in the input field user can add a maximum of 2 characters
		And After selecting/adding complete die bin details click on the "Add Die/Bin Detail" button
		And All the details of Die/Bin will be added in the "Saved Die/Bin Details" section
		And Navigate into the "Output" tab
		And Enter "Main Directory" folder path in Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter file name format in input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check the "Output Destination Of Assembly Map File" to make sure that path has been added
		And Click on the "Save and generate Assembly Map" button
		Then Verify that a new assembly map wafer was saved into the database with MA1 wafer

#		Following steps are related to desktop app that is why these cannot be automated
#		And Verify that a AMG file is saved into the given path


	@YWPD-TC-932 @retry
	Scenario Outline: YWPD-TC-932 - Verify that user is able to Generate a Manual Assembly/Pick Map on Calculated wafer/Die Size Settings
	The objective of this test case is to ensure that users can successfully generates the Manual Assembly/Pick Map with Small Data Set favorite selection. Additionally, this test case aims to validate the functionality of Generates Manual Assembly/Pick Map and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		When Open Generate Manual Assembly/Pick Map
		And Select the data set size as "<Data Set Size>" and facility as "<Facility>"
		And After selecting facility, work center, device, test program, lot and wafer will be selected automatically
		And Select the "<Wafer ID>" from wafers
		And Select Wafer plotting option as "<Wafer Plotting Option>"
		And Click on the Plot Wafer Map to Pick Map Die(S)
		And User will be redirected to the Bin Wafer Map screen
		And Select the few wafer dies (as seen in the attached images)
		And Click on the plus sign available at the end on right side and expand the options
		And Select mark as assemble from the option
		And "Selected dies have been marked as assembled" message will appear and selected dies will be marked
		And Again click on the plus sign available at the end on the right side and expand the options
		And Click on the "Save and generate AMG"
		And User will be redirected to "Generations" tab
		And Choose the "<Conversion of Assembly Map File to Format>" format
		And Navigate into the "Output" tab
		And Enter the "<Main Directory>" folder path in Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter file name format in input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check "Output Destination Of Assembly Map File" to make sure that path has been added
		And Click on the "Save and generate Assembly Map" button
		Then Verify that the new assembly map wafer was saved into the database with MA1 wafer

#		Following steps are related to desktop app that is why these cannot be automated
#		Then Then verify that a MA1 Wafer is saved into the desktop application
#		And Open desktop application
#		And Click the Wafer Map Report icon
#		And Select the <Data Set Size> and MA1 wafer and execute report
#		Then Verify the <Expected MA1 Wafer>, <Expected MA1 Wafer Legend> and <Expected MA1 Wafer File> is saved into the given path

	Examples:
		| Data Set Size  | Facility           | Wafer ID | Wafer Plotting Option              | Conversion of Assembly Map File to Format | Main Directory | If Assembly Map File Exists | File Name Format          | Output Path         | Expected MA1 Wafer            | Expected MA1 Wafer Legend           | Expected MA1 Wafer File             |
		| Small Data Set | WEB SMALL DATA SET | 1        | Calculated Wafer/Die Size Settings | ASCII TMA                                 | D:\MA1         | Rename Old and Create New   | @FacilityID, @Date, @Time | Local/Network Drive | AMG_SD_WSDS_1_CW_MA1Wafer.png | AMG_SD_WSDS_1_CW_MA1WaferLegend.png | AMG_SD_WSDS_1_CW_MA1WaferLegend.tma |


	@YWPD-TC-931 @retry
	Scenario: YWPD-TC-931 - Verify that the user is able to Generate a Manual Assembly/Pick Map on Actual Wafer/Die Size Settings
	Verify that the user is able to Generate a Manual Assembly/Pick Map on Actual Wafer/Die Size Settings
		Given The user successfully opened the yieldWerx web application and login
		When Open Generate Manual Assembly/Pick Map
		And Select the facility data
		And After selecting facility, work center, device, test program, lot and wafer will be selected automatically
		And Select the Wafer plotting option as "Actual Wafer/Die Size Settings"
		And Click on the Plot Wafer Map to Pick Map Die(s)
		And User will be redirected to the Bin Wafer Map screen
		And Select the few wafers die
		And Click on the plus sign available at the end on right side and expand the options
		And Select mark as assemble from the option
		And "Selected dies have been marked as assembled" message will appear and selected dies will be marked
		And Again click on the plus sign available at the end on the right side and expand the options
		And Click on the "Save and generate AMG"
		And User will be redirected to "Generations" tab
		And Choose the AMG format from "Conversion of Assembly Map File to Format"
		And Navigate into the "Output" tab
		And Enter "Main Directory" folder path in Input field
		And Select the options from "<If Previous Assembly Map File Exists>"
		And Enter file name format in input field, Enter @ in the input field options will be visible select any option from the list
		And Choose the output path from the available Options: (Local/Network Drive, FTP Drive, SFTP Drive)
		And Click on the "Add Path" button
		And Check the "Output Destination Of Assembly Map File" to make sure that path has been added
		And Click on the "Save and generate Assembly Map" button
		Then Verify that a new assembly map wafer was saved into the database with MA1 wafer


#		Following step is related to desktop app that is why these cannot be automated
#		Then Verify that an AMG file is saved into the given path


	@YWPD-TC-933 @retry
	Scenario: Verify that user is able to Generate Manual Assembly/Pick Map on FTP/SFTP server
	The objective of this test case is to ensure that users can successfully  Generate Manual Assembly/Pick Map on FTP/SFTP server
		Given The user successfully opened the yieldWerx web application and login
		When Open Generate Manual Assembly/Pick Map
		And Select the facility data
		And After selecting facility, work center, device, test program, lot and wafer will be selected automatically
		And Select the Wafer plotting option as "Actual Wafer/Die Size Settings"
		And Click on the Plot Wafer Map to Pick Map Die(s)
		And User will be redirected to the Bin Wafer Map screen
		And Select the few wafers die
		And Click on the plus sign available at the end on right side and expand the options
		And Select mark as assemble from the option
		And "Selected dies have been marked as assembled" message will appear and selected dies will be marked
		And Again click on the plus sign available at the end on the right side and expand the options
		And Click on the "Save and generate AMG"
		And User will be redirected to "Generations" tab
		And Choose the AMG format from "Conversion of Assembly Map File to Format"
		And Navigate into the "Output" tab
		And Enter the file name format into the input field, Enter @ in the input field options will be visible select any option from the list for SFTP option
		And Choose the output path as (FTP Drive/SFTP Drive)
		And Enter the user name as "sftp" and password as "Trisoft@123" for FTP/SFTP drive
		And Enter the path of FTP/SFTP Drive into the main directory input field
		And Click on the "Add Path" button
		And Check on the "Output Destination Of Assembly Map File" that the path has been added
		And Click on the "Save and generate Assembly Map" button
		Then Verify that A new assembly map wafer was saved into the database with MA1 wafer


#		Following step is related to desktop app that is why these cannot be automated
#		And Verify that the AMG file was saved into the given path of FTP/SFTP


	@YWPD-TC-929 @retry
	Scenario: Verify that user is able to Reset the Manual AMG Policy Grid Selection
	The objective of this test case is to ensure that users can successfully Reset the Manual AMG Policy Grid Selection
		Given The user successfully opened the yieldWerx web application and login
		When Open Manual AMG Policy Execution
		And Select facility data to generate Assembly Maps
		And After selecting the data facility, Work Center, Device, Test Program, Lot, and policy should be selected automatically
		And Select the wafers to generate their Assembly Maps
		And Click the Reset Button
		Then Verify that All the data selections will be reset


	@YWPD-TC-928 @retry
	Scenario Outline: Verify that user is able to Generate a Manual AMG Policy successfully
	The objective of this test case is to ensure that users can successfully generate Manual Assembly Map with Small Data Set favorite selection. Additionally, this test case aims to validate the functionality of Manual AMG Policy Execution and associated UI options.
		Given The user successfully opened the yieldWerx web application and login
		And Create New Assembly Map Policies as a Pre-Requisite
		When Open Manual AMG Policy Execution
		And Select "<Data Set Size>", and "<Facility>" to generate Assembly Maps
		And After selecting facility, work center, device, test program, lot and wafer will be selected automatically
		And Choose the Policies of your choice
			| Policies   |
			| <Policies> |
		And Select the wafers to generate their Assembly Maps
		And Click on Generate Policy Based Assembly Map
		And Assembly Map Generated Successfully message appears
		And Delete the created policies as post-requisite


#		Following steps are related to desktop app that is why these cannot be automated
#		Then Verify that the MA wafer is saved into the desktop application and File will also be downloaded into the path provided in the policy
#		And Open desktop application
#		And Click the Wafer Map Report icon
#		And Select the <Data Set Size> and MA wafer and execute report
#		And Verify the <Expected MA Wafer>, <Expected MA Wafer Legend> with wafer ID 1 and <Expected MA Wafer File>

		Examples:
		| Data Set Size | Facility           | Policies                  | Expected MA Wafer       | Expected MA Wafer Legend      | Expected MA Wafer File      |
		| Small Data    | WEB SMALL DATASET  | Test Program Level Policy | AMG_SD_TPLP_MAWafer.png | AMG_SD_TPLP_MAWaferLegend.png | AMG_SD_TPLP_MAWaferFile.tma |
		| Small Data    | WEB SMALL DATASET  | Device Level Policy       | AMG_SD_DLP_MAWafer.png  | AMG_SD_DLP_MAWaferLegend.png  | AMG_SD_DLP_MAWaferFile.tma  |


	@YWPD-TC-929 @retry
	Scenario: Verify that user is able to Reset the Manual AMG Policy Grid Selection
	The objective of this test case is to ensure that users can successfully Reset the Manual AMG Policy Grid Selection
		Given The user successfully opened the yieldWerx web application and login
		When Open Manual AMG Policy Execution
		And Select facility data to generate Assembly Maps
		And After selecting the data facility, Work Center, Device, Test Program, Lot, and policy should be selected automatically
		And Select the wafers to generate their Assembly Maps
		And Click the Reset Button
		Then Verify that All the data selections will be reset