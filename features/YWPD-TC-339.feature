Feature: PAT

	@YWPD-TC-339
	Scenario: Verify that user is able to generate the Static PAT Test Program Level Rule
		Given Click on say "Quality & PAT" in the left menu bar
#		When Click on PAT Rules
#		And Click 'New Static PAT' button from PAT Rules window
#		And Create PAT Rule window will be open and enter rule <Name> and description in 'General' tab
#		And Navigate into the parameters tab and select the <Data Set Size> and <Facility>
#		And After selecting <Facility> data will be populated automatically for work center, device and test program
#		And Select the <Parameter Number>
#		And Keep default settings for 'Validate PAT Limits Against' check box
#		And Select Bin Type from 'Hard Bin/Soft Bin' drop down
#		And Navigate into the 'Static Limits' tab and enter value for <Low Seed Limit> and <High Seed Limit>
#		And Click on the 'Calculate Seed' button Create PAT Rule window will open after clicking 'Calculate Seed' button and available Lots will appear
#		And Select Lot and click 'Calculate' button and value for <Low Seed Limit> and <High Seed Limit> will be calculated automatically
#		And Enter the lot number for <After Every Lots>
#		And Provide the <Value of K>
#		And Select option from <PAT Limit to Apply> dropdown
#		And Provide <Hard Bin Number for Lower PAT limit >, <Soft Bin Number for Lower PAT limit>, <Hard Bin Number for Upper PAT limit>, and <Soft Bin Number for Upper PAT limit>
#		And Click 'Save' button
#		Then The rule will be saved and appear in the PAT Rules window and PAT_RulesDetails table in database
#        Examples:
#		  | Data Set Size  | Name                            | Facility           | Parameter Number                | Low Seed Limit    | High Seed Limit    | After Every Lots | Value of K | PAT limit to Apply              | Hard Bin Number for Lower PAT limit  | Soft Bin Number for Lower PAT limit  |  Hard Bin Number for Upper PAT limit | Soft Bin Number for Upper PAT limit |
#		  | Small Data Set | Static Test program level rule  | WEB SMALL DATA SET | 2, Idd_prewrite Idd_prewrite 26 | 6.502738888888891 | 14.922961111111107 | 8                | 6          | Both (Lower & Upper) PAT Limit  | 22                                   | 22                                   | 44                                   | 44                                  |