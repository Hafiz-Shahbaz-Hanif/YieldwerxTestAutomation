Feature: SWM Policies

	@YWPD-TC-328 @retry
	Scenario Outline: YWPD-TC-328 - Verify that the user is able to create SWM Policy at Test Program Level with web small dataset
	The objective of this test case is to ensure that the users can successfully create SWM Policy at Test Program Level with web small dataset
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When Click New SWM Policy button from SWM Policies window
		When Create SWM Policy Window will open
		When Enter "<Name>" And description in "General" tab
		When Click "Input Data & Rule Selection" And Select "<Level>" from dropdown
		When Select the Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select Source Device as "<Source Device>"
		When Select Source Probe as "(1|M)" and Source Test Program as "<Source Test Program>"
		When Select Target Facility  as "<Target Facility>", Target Work Center  as "<Target Work Center>
		When Select Target Device as "<Target Device>"
		When Select Target Test Program as "<Target Test Program>", Target Probe "(1|M)"
		When Select "<Rules>" from the Rules section
		When Click "Output Data Selection" tab and provide all the information like
			 """
			 Metadata Selection From, Merge Facility, Merge Work Center, Merge Device, Merge Test Program
			 """
		When Enter the information for
			 """
			 Source Parameter Prefix, Target Parameter Prefix,
			 Delta Parameter Prefix in 'Parameter Generation Option' tab if required otherwise keep it as default
			 """
		When Enter the information for "Wafer Rotation" like
			 """
	  		 'Rotate Wafer, Apply Offset, Include Die Types' if required otherwise keep it as default
	  		 """
		When Select Die Type Details by using checkbox
		When Click Manage Exception tab and select the required option otherwise keep it as default
		When Click Save button to save the new created policy
		Then Verify that the policy has been saved and appears in the SWM Policies window
			 """
			 and in "SWMPolicies" table in database
			 """

	Examples:
		| Name                   | Level        | Source Facility   | Source Work Center | Source Device | Source Test Program | Target Facility    | Target Work Center | Target Device | Target Test Program | Rules                                                                                                                                             |
		| SWM_Policy_TestProgram | Test Program | WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATA SET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | 4670-PrePostMerge-P-P _TestProgram, 4670-PrePostMerge-F-F - TestProgram, 4670-PrePostMerge-P-F - TestProgram, 4670-PrePostMerge-F-P - TestProgram |


	@YWPD-TC-336 @retry
	Scenario Outline: YWPD-TC-336 - Verify that the user is able to automate SWM Policies successfully with web small
	dataset
	The objective of this test case is to ensure that the users can successfully automate SWM Policies with web small dataset. Additionally, this test case aims to validate the functionality of saved auto SWM wafer (C) in yieldWerx desktop application through Wafer Map Report.
		Given The user is successfully logged in the yieldWerx web application
		When Click on "SWM" in the left menu bar
		When Click "Automate SWM Policies" and new window will open
		When Click on "Automate SWM Policy" and Create Automate SWM Policy window will open
		When Select Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select the Source Device as "<Source Device>" and the Source Test Program as "<Source Test Program>"
		When Select the Target Facility as "<Target Facility>", Target Work Center as "<Target Work Center>"
		When Select the Target Device as "<Target Device>" and the Target Test Program as "<Target Test Program>"
		When Select policy from Policies as "<Policies>" section and click on "Save" button
		When SWM Policy has been created and displayed in "Automate SWM Policies" window
		When Enable check box available infront of each created Automate SWM Policy in Automate SWM Policies window to automate the policy
		Then Verify that the policy will be automated with success message


		# following steps of this scenario are related to desktop app
#		When Combine wafer (C) will be saved in yieldWerx desktop application against selection
#		When Select wafer table in database, provide Lot_Sequence, and see the C wafer with probing sequence = -8
#		When Open yieldWerx desktop application and open Bin Wafer Map report
#		When Select that facility where SWM Combine Wafer Map has been saved
#		When Combine wafer has been displayed with probe count C against the selected facility
#		Then Verify the <Expected Chart>
#		When Click Legend button available in right bottom right corner of generated chart of C wafer in gallery view
#		Then Verify the <Expected Legend>

	Examples:
		| Source Facility   | Source Work Center | Source Device | Source Test Program | Target Facility   | Target Work Center | Target Device | Target Test Program | Policies          | Expected Chart                                                                      | Expected Legend                                                                                                                                                  |
		| WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | 4670 Test Program | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 Test Program_WM_C_Chart.jpg | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 Test Program_WM_C_Legend.jpg                                                                             |
#		| WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | 4670 device       | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_WM_C_Chart.jpg       | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_WM_C_Legend1.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_WM_C_Legend2.jpg |


	@YWPD-TC-337 @retry
	Scenario: YWPD-TC-337 -Verify that the user is able to Un-Automate SWM Policies with web small dataset
	The objective of this test case is to ensure that the users can successfully Un-Automate SWM Policies with web small dataset.
		Given The user is successfully logged in the yieldWerx web application
		When Click on "SWM" in the left menu bar
		When Click "Automate SWM Policies" and new window will open
		When See the list of already created Automate SWM Policies
		When Uncheck the check box available infront of already automated SWM Policy
		When Confirmation Required pop-up window with options "Yes, No, Cancel" will open
		When Click Yes to un-automate the Policy
		Then Verify that the policy will be un-automated and window of Automate SWM Policies will be refresh


	@YWPD-TC-338 @retry
	Scenario: YWPD-TC-338 - Verify that the user is able to delete automated SWM Policies successfully with web small
	dataset
	The objective of this test case is to ensure that the users can successfully delete automated SWM Policies with web small dataset.
		Given The user is successfully logged in the yieldWerx web application
		When Click on "SWM" in the left menu bar
		When Click "Automate SWM Policies" and new window will open
		When See the list of already created Automate SWM Policies
		When Click the "Delete" button available at the end of already created and automated SWM Policy
		When Confirmation Required pop-up window with options "Yes, No, Cancel" will open
		When Click Yes to delete the policy
		Then Verify that the policy will be deleted from Automate SWM Policies window
#		Then The policy will remove from "SWMAutomatedPolicies" table in database


	@YWPD-TC-334 @retry
	Scenario Outline: YWPD-TC-334 - Verify that the user is able to create Manual SWM successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully create Manual SWM with web small dataset
		Given The user is successfully logged in the yieldWerx web application
		When Click "SWM" in the left menu bar
		When Click "Manual SWM" and Manual SWM window will open
		When Click and select "<Source Facility>", the "<Source Work Center>", "<Source Device>", "<Source Test Program>"
		When Select Source Lots (73631), Source Wafers (Probe Count = 1)
		When Click and select "<Target Facility>", "<Target Work Center>", "<Target Device>", "<Target Test Program>"
		When Select Target Lots (73631), Target Wafers (Probe Count = 1), "<Policies>"
		When Select "Wafer Plotting Option" from "Calculated Wafer/Die Size Settings and Actual Wafer/Die Size Setting"
		When Click "Generate Manual SWM" button to generate Manual SWM Wafer
		Then Manual SWM Wafer as Combine Bin Wafer Map with Wafer ID: MC will be generated and be shown

# Following steps are related to desktop app and also involve data verification from attached images:
#		Then Verify the <Expected Chart>
#		And Click 'Legend' button to see the legend for generated Manual SWM Wafer (MC)
#		Then Verify the <Expected Legend>
#		And Click 'Zoom' button to see the generated Manual SWM Wafer and Manual SWM Wafer will open in new window
#		And verify header information and Die Details information with the Manual SWM Wafer in gallery view window
#		And Click 'Chart Context Menu' button available at the right corner of X axis of chart
#		And Click any option from 'Print Chart, Download PNG image, Download SVG vector image, Download CSV, and Downoad XLS' avialable in 'Chart Context Menu'
#		And Click 'Plotting Options' button available in top left corner in zoom in window of Manual SWM Wafer
#		And Click 'Die Type Color' button available under 'Plotting Options' and select one option from 'Bin Color, Die Type Color, and Both' and click apply button and made changes will applied to the chart
#		And Select/Unselect 'Die Type' by enabling check box available for each type or by 'Select All and Unselect All' button available below 'Die Type Filters' in 'Die Color Type' button and click 'Apply'
#		And All the made changes will apply on the chart
#		And Click 'Point Labels' button available under 'plotting Options' and select one option from 'None, Reticle Site Number, and Reticle Outline' and click 'Apply'
#		And All the made changes will apply on the chart
#		And Go back from zoom in window to gallery view window of Manual SWM Wafer
#		And Click 'SAVE TO YIELDWERX' button available at top right side of generated Manual SWM window to save the Manual SWM Wafer as Combine Bin Wafer Map with ID: MC to desktop application
#		Then Verify that the Manual SWM Wafer as Combine Bin Wafer Map with Wafer ID: MC will be saved to desktop application and you will see a successful message
#		And Select wafer table in database, provide Lot_Sequence, and see the MC wafer with probing sequence = -10
#		And Open yieldWerx desktop application and open Bin Wafer Map report
#		And Select that facility for which generated Manual SWM as Combine Bin Wafer Map with ID: MC was saved
#		And Select Work Center (WAFER SORT_WAFER SORT), Device Name (4670), Test Program (PREBAKE_A_4670_POSTBAKE_A_4670), Lot and saved wafer (MC) will appear in wafer table
#		And See the Wafer table in 'P' column, Manual SWM as Combine Bin Wafer Map with ID: MC will be available and select this wafer and execute the report
#		Then Verify the <Expected Chart>
#		And Click 'Legend' button to see the legend for generated Manual SWM Wafer (MC)
#		Then Verify the <Expected Legend>

	Examples:
		| Source Facility   | Source Work Center | Source Device | Source Test Program | Target Facility   | Target Work Center | Target Device | Target Test Program | Policies          | Expected Chart                                                                                                                                                    | Expected Legend                                                                                                                                                                                                                                                                                                                                                                                  |
		| WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | 4670 Test Program | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 Test Program_Chart.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_WM_4670 Test Program_Chart.jpg | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 Test Program_Legend1.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 Test Program_Legend2.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_WM_4670 Test Program_Legend.jpg


	@YWPD-TC-335 @retry
	Scenario: Verify that the user is able to Edit Policy from Manual SWM successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully Edit Policy from Manual SWM with web small dataset
		Given The user is successfully logged in the yieldWerx web application
		When Click "SWM" in the left menu bar
		When Click "Manual SWM" and Manual SWM window will open
		When Click and select Source Facility, the Source Work Center, Source Device, Source Test Program
		When Select Source Lots (73631), Source Wafers (Probe Count = 1)
		When Click and select Target Facility, Target Work Center, Target Device, Target Test Program
		When Select Target Lots (73631), Target Wafers (Probe Count = 1), "<Policies>"
		When Select "Wafer Plotting Option" from "Calculated Wafer/Die Size Settings and Actual Wafer/Die Size Setting"
		When Click "Generate Manual SWM" button to generate Manual SWM Wafer
		Then Manual SWM Wafer as Combine Bin Wafer Map with Wafer ID: MC will be generated and be shown
		When Click "Edit Policy" button available top right side of window
		When Create SWM Policy window will open and make changes in General, Input Data & Rule selection, Output Data Selection, and Manage exceptions tab that you want to modify
		When Click "Save" button and Save Change
		When After popup appears choose any option and click "OK" button to save the changes
		Then Verify that the policy with made changes will be saved and Manual SWM will refresh


	@YWPD-TC-331 @retry
	Scenario: YWPD-TC-331 - Verify that the user is able to Modify SWM Policy successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully Modify SWM Policy with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When See the list of already created SWM policies
		When Click "Edit" button available for each policy
		When Create SWM Policy Window will open
		When Change the "Name" and "Description" in "General" tab
		When Make changes that you want in tabs
			 """
			 "General" tab, "Input Data & Rule Selection", "Output Data Selection" and "Manage Exceptions"
			 """
		Then Verify that the edited policy has been saved and appears in the SWM Policies window
			 """
			 and in "SWMPolicies" table in database
			 """


	@YWPD-TC-333 @retry
	Scenario: YWPD-TC-333 - Verify that the user is able to Copy SWM Policy with web small dataset
	The objective of this test case is to ensure that the users can successfully Copy SWM Policy with web small dataset
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When See the list of already created SWM policies
		When Click Copy button available infront of each already created policy
		When Create SWM Policy Window will open
		When Change name and description from in the General tab
		When Make required changes in tabs
			 """
			 "General" tab, "Input Data & Rule Selection", "Output Data Selection" and "Manage Exceptions"
			 """
		Then Verify that the copied policy has been saved and appears in the SWM Policies window
			 """
			 and in "SWMPolicies" table in database
			 """

	@YWPD-TC-332 @retry
	Scenario: YWPD-TC-332 - Verify that the user is able to delete SWM Policy successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully delete SWM Policy with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When See the list of already created SWM policies
		When Click delete button available at the end of each policy
		When Confirmation Required pop-up window will appear, with "Yes" and "No" buttons
		When Click "Yes" to delete the policy
		Then Verify that the policy will be deleted
			 """
			 and window will be refresh and the deleted policy removed from "SWMPolicies" table in database
			 """


	@YWPD-TC-332 @retry
	Scenario: YWPD-TC-332 - Verify that the user is able to delete SWM Policy successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully delete SWM Policy with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When See the list of already created SWM policies
		When Click delete button available at the end of each policy
		When Confirmation Required pop-up window will appear, with "Yes" and "No" buttons
		When Click "Yes" to delete the policy
		Then Verify that the policy will be deleted
			 """
			 and window will be refresh and the deleted policy removed from "SWMPolicies" table in database
			 """


	@YWPD-TC-330 @retry
	Scenario Outline: YWPD-TC-330 - Verify that the user is able to create SWM Policy at Device Level Custom Test Program with web small dataset
	The objective of this test case is to ensure that the users has successfully created SWM Policy on Device Level Custom Test Program with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When Click New SWM Policy button from SWM Policies window
		When Create SWM Policy Window will open
		When Enter "<Name>" And description in "General" tab
		When Click "Input Data & Rule Selection" And Select "<Level>" from dropdown
		When Select "<Test Program Options>" as Custom
		When Select the Source Facility as "<Source Facility>", Source Work Center as "<Source Work Center>"
		When Select Source Device as "<Source Device>"
		When Select "(1|M)" as a Source Probe
		When Select Target Facility  as "<Target Facility>", Target Work Center  as "<Target Work Center>
		When Select Target Device as "<Target Device>"
		When Select the "(1|M)" option as Target Probe
		When Select "<Rules>" from the Rules section
		When Click on Manage Test Programs Hyperlink and provide Test Programs Mapping
		When Select Source Test Program and Target Test Program from their respective dropdowns and click Add button
		When Click Apply button after adding
			 """
			 Source Test Program and Target Test Program,
	 		 Test Program Mapping has been applied
	 		 """
		When Click "Output Data Selection" tab and provide all the information like
			 """
			 Metadata Selection From, Merge Facility, Merge Work Center, Merge Device, Merge Test Program
			 """
		When Enter the information for
			 """
			 Source Parameter Prefix, Target Parameter Prefix,
			 Delta Parameter Prefix in 'Parameter Generation Option' tab if required otherwise keep it as default
			 """
		When Enter the information for "Wafer Rotation" like
			 """
	  		 'Rotate Wafer, Apply Offset, Include Die Types' if required otherwise keep it as default
	  		 """
		When Select Die Type Details by using checkbox
		When Click Manage Exception tab and select the required option otherwise keep it as default
		When Click Save button to save the new created policy
		Then Verify that the policy has been saved and appears in the SWM Policies window
			 """
			 and in "SWMPolicies" table in database
			 """

	Examples:
		| Name                     | Level  | Test Program Options | Source Facility    | Source Work Center | Source Device | Target Facility    | Target Work Center | Target Device | Rules                                                                                                                                                                                                                                                                                                                                              |
		| SWM_Policy_Device_Custom | Device | Custom               | WEB SMALL DATA SET | WAFER SORT         | 4670          | WEB SMALL DATA SET | WAFER SORT         | 4670          | 4670-PrePostMerge-P-P, 4670-PrePostMerge-P-F, 4670-PrePostMerge-F-P, 4670-PrePostMerge-F-F, 4670-PrePostMerge-Missing-Missing, 4670-PrePostMerge-P-Missing, 4670-PrePostMerge-Missing-P, 4670-PrePostMerge-F-Missing, 4670-PrePostMerge-Missing-F, 4670-PrePostMerge-P-NA, 4670-PrePostMerge-F-NA, 4670-PrePostMerge-NA-P, 	4670-PrePostMerge-NA-F |


	@YWPD-TC-334 @retry
	Scenario Outline: YWPD-TC-334 - Verify that the user is able to create Manual SWM successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully create Manual SWM with web small dataset
		Given The user is successfully logged in the yieldWerx web application
		When Click "SWM" in the left menu bar
		When Click "Manual SWM" and Manual SWM window will open
		When Click and select "<Source Facility>", the "<Source Work Center>", "<Source Device>", "<Source Test Program>"
		When Select Source Lots (73631), Source Wafers (Probe Count = 1)
		When Click and choose "<Target Facility>", "<Target Work Center>", "<Target Device>", "<Target Test Program>"
		When Select Target Lots (73631), Target Wafers (Probe Count = 1), "<Policies>"
		When Select "Wafer Plotting Option" from "Calculated Wafer/Die Size Settings and Actual Wafer/Die Size Setting"
		When Click "Generate Manual SWM" button to generate Manual SWM Wafer
		Then Manual SWM Wafer as Combine Bin Wafer Map with Wafer ID: MC will be generated and be shown

	Examples:
	| Source Facility   | Source Work Center | Source Device | Source Test Program | Target Facility   | Target Work Center | Target Device | Target Test Program | Policies          | Expected Chart                                                                                                                                                    | Expected Legend                                                                                                                                                                                                                                                                                                                                                                                  |
	| WEB SMALL DATASET | WAFER SORT         | 4670          | PREBAKE_A_4670      | WEB SMALL DATASET | WAFER SORT         | 4670          | POSTBAKE_A_4670     | 4670 device       | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_Chart.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_WM_4670 device_Chart.jpg             | WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_Legend1.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_Legend2.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_4670 device_Legend3.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_WM_4670 device_Legend1.jpg, WSDS_4670_PREBAKE_A_4670_WSDS_4670_POSTBAKE_A_4670_WM_4670 device_Legend2.jpg |


	@YWPD-TC-332 @retry
	Scenario: YWPD-TC-332 - Verify that the user is able to delete SWM Policy successfully with web small dataset
	The objective of this test case is to ensure that the users can successfully delete SWM Policy with web small dataset.
		Given The user successfully opened the yieldWerx web application and login
		When Click on "SWM" in the left menu bar and click on SWM Policies
		When See the list of already created SWM policies
		When Click delete button available at the end of each policy
		When Confirmation Required pop-up window will appear, with "Yes" and "No" buttons
		When Click "Yes" to delete the policy
		Then Verify that the policy will be deleted
			 """
			 and window will be refresh and the deleted policy removed from "SWMPolicies" table in database
			 """