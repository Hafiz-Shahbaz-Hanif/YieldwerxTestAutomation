import pyodbc
import json
from decimal import Decimal
from datetime import datetime
from utilities.Exceptions import MyException
from utilities.customLogger import LogGen


class PF_DBQueries:
    logger = LogGen.loggen()

    def __init__(self):
        conn_string = (
            'DRIVER={ODBC Driver 18 for SQL Server};'
            'SERVER=YWSRV2\YWSRV2019;'
            'DATABASE=yw_V4_Automation_4_2_25_0_AhsanMughal;'
            'UID=sa;'
            'PWD=subway3328;'
            'TrustServerCertificate=yes;'
        )
        self.conn = pyodbc.connect(conn_string)
        self.cursor = self.conn.cursor()

    def dataWaferTable(self, context):
        try:
            # Hardcoded expected results
            expected_results = {
                "Wafer_Sequence": 105,
                "Lot_Sequence": 67,
                "Wafer_ID": "5",
                "Part_Count": 714,
                "Good_Count": 640,
                "Probing_Sequence": 1,
                "Total_Unique_Dies": 741,
                "Yield": 86.3697705802969
            }

            # Query to fetch wafer data from database
            query_result = self.cursor.execute("SELECT * FROM WAFER WHERE Wafer_Sequence='105'").fetchone()

            # Store the result in the context if needed
            context.wafer_details_from_db = query_result

            self.logger.info("Query Wafer executed successfully")

            # Convert the Row object to a dictionary
            if query_result:
                wafer_table_column_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(wafer_table_column_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime, and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of Wafer:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            Wafer_Sequence = result_dict.get("Wafer_Sequence", None)
            Lot_Sequence = result_dict.get("Lot_Sequence", None)
            Wafer_ID = result_dict.get("Wafer_ID", None)
            Part_Count = result_dict.get("Part_Count", None)
            Good_Count = result_dict.get("Good_Count", None)
            Probing_Sequence = result_dict.get("Probing_Sequence", None)
            Total_Unique_Dies = result_dict.get("Total_Unique_Dies", None)
            Yield = result_dict.get("Yield", None)

            # Compare query results with expected results
            comparison_results = {
                "Wafer_Sequence": Wafer_Sequence == expected_results["Wafer_Sequence"],
                "Lot_Sequence": Lot_Sequence == expected_results["Lot_Sequence"],
                "Wafer_ID": Wafer_ID == expected_results["Wafer_ID"],
                "Part_Count": Part_Count == expected_results["Part_Count"],
                "Good_Count": Good_Count == expected_results["Good_Count"],
                "Probing_Sequence": Probing_Sequence == expected_results["Probing_Sequence"],
                "Total_Unique_Dies": Total_Unique_Dies == expected_results["Total_Unique_Dies"],
                "Yield": Yield == expected_results["Yield"]
            }

            # Print and log the comparison results
            for key, match in comparison_results.items():
                if match:
                    self.logger.info(f"{key} matches expected value.")
                else:
                    self.logger.error(f"{key} does NOT match expected value. Expected: {expected_results[key]}, Found: {result_dict.get(key)}")

            # Store the result in context if needed
            context.wafer_details_from_db = query_result_dict
            self.logger.info(f"Query Wafer executed successfully with comparison results: {comparison_results}")

        except Exception as e:
            self.logger.error("Error in dataWaferTable: %s", e)
            MyException.handle_exception(context, e)

    def dataSWMRule(self, context):
        try:
            # Define hardcoded expected results
            expected_results = {
                "ID": 5270,  # Example ID
                "Name": "Randy Lara",
                "Level": "Test Program",
                "Version": "1.0",
                "SourceFacility": "WEB SMALL DATASET",
                "SourceWorkCenter": "WAFER SORT",
                "SourceDevice": "4670",
                "SourceTestProgram": "PREBAKE_A_4670",
                "SourceProbes": "1|M",
                "TargetFacility": "WEB SMALL DATASET",
                "TargetWorkCenter": "WAFER SORT",
                "TargetDevice": "4670",
                "TargetTestProgram": "POSTBAKE_A_4670",
                "TargetProbes": "1|M"
            }

            # Query SQL Server and retrieve data
            query_result = self.cursor.execute("SELECT * FROM SWMRules ORDER BY 1 DESC").fetchone()

            # Store the result in the context if needed
            context.swm_rules_details_from_db = query_result
            self.logger.info("Query SWM Rule executed successfully")

            # Convert the Row object to a dictionary
            if query_result:
                swm_rule_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(swm_rule_table_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of SWM Rules:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            SWMR_ID = result_dict.get("ID", None)
            SWMR_Name = result_dict.get("Name", None)
            SWMR_Level = result_dict.get("Level", None)
            SWMR_Version = result_dict.get("Version", None)
            SWMR_SourceFacility = result_dict.get("SourceFacility", None)
            SWMR_SourceWorkCenter = result_dict.get("SourceWorkCenter", None)
            SWMR_SourceDevice = result_dict.get("SourceDevice", None)
            SWMR_SourceTestProgram = result_dict.get("SourceTestProgram", None)
            SWMR_SourceProbes = result_dict.get("SourceProbes", None)
            SWMR_TargetFacility = result_dict.get("TargetFacility", None)
            SWMR_TargetWorkCenter = result_dict.get("TargetWorkCenter", None)
            SWMR_TargetDevice = result_dict.get("TargetDevice", None)
            SWMR_TargetTestProgram = result_dict.get("TargetTestProgram", None)
            SWMR_TargetProbes = result_dict.get("TargetProbes", None)

            # Compare fetched results with expected results
            comparison_results = {
                "ID": (SWMR_ID == expected_results["ID"]),
                "Name": (SWMR_Name == expected_results["Name"]),
                "Level": (SWMR_Level == expected_results["Level"]),
                "Version": (SWMR_Version == expected_results["Version"]),
                "SourceFacility": (SWMR_SourceFacility == expected_results["SourceFacility"]),
                "SourceWorkCenter": (SWMR_SourceWorkCenter == expected_results["SourceWorkCenter"]),
                "SourceDevice": (SWMR_SourceDevice == expected_results["SourceDevice"]),
                "SourceTestProgram": (SWMR_SourceTestProgram == expected_results["SourceTestProgram"]),
                "SourceProbes": (SWMR_SourceProbes == expected_results["SourceProbes"]),
                "TargetFacility": (SWMR_TargetFacility == expected_results["TargetFacility"]),
                "TargetWorkCenter": (SWMR_TargetWorkCenter == expected_results["TargetWorkCenter"]),
                "TargetDevice": (SWMR_TargetDevice == expected_results["TargetDevice"]),
                "TargetTestProgram": (SWMR_TargetTestProgram == expected_results["TargetTestProgram"]),
                "TargetProbes": (SWMR_TargetProbes == expected_results["TargetProbes"])
            }

            # Print and log the comparison results
            for key, match in comparison_results.items():
                if match:
                    self.logger.info(f"{key} matches expected value.")
                else:
                    self.logger.error(
                        f"{key} does NOT match expected value. Expected: {expected_results[key]}, Found: {result_dict.get(key)}")

            # Store the result in context if needed
            context.wafer_details_from_db = query_result_dict
            self.logger.info(f"Query SWM Rules executed successfully with comparison results: {comparison_results}")

        except Exception as e:
            self.logger.error("Error in dataWaferTable: %s", e)
            MyException.handle_exception(context, e)

    def dataSWMPolicy(self, context):
        try:
            # Define hardcoded expected results
            expected_results = {
                "ID": 2092,  # Example ID
                "Name": "SWM_Policy_Device_CustomAaron Young",
                "Level": "Device",
                "Version": "1.0",
                "SourceFacility": "WEB SMALL DATASET",
                "SourceWorkCenter": "WAFER SORT",
                "SourceDevice": "4670",
                "SourceTestProgram": "NULL",
                "SourceProbes": "1|M",
                "TargetFacility": "WEB SMALL DATASET",
                "TargetWorkCenter": "WAFER SORT",
                "TargetDevice": "4670",
                "TargetTestProgram": "NULL",
                "TargetProbes": "1|M",
                "MergeFacility": "WEB SMALL DATASET",
                "MergeWorkCenter": "WAFER SORT_WAFER SORT",
                "MergeDevice": "4670",
                "MergeTestProgram": "@Source.TestProgram_@Target.TestProgram",
                "MergeProbes": "C",
                "ProceedIfSWaferNotExist": 0,
                "ProceedIFTWaferNotExist": 0,
                "SWMDieTypeID": 1,
                "IgnoreTestTemperature": 1,
                "SourceDieTypes": "12,13,14,15,18,19",
                "TargetDieTypes": "12,13,14,15,18,19",
                "ParametricDataCopyID": 3
            }

            # Query to retrieve SWM Policy Data
            query_result = self.cursor.execute("SELECT * FROM SWMPolicies ORDER BY 1 DESC").fetchone()
            self.logger.info("Query Result of SWM Policy: %s", query_result)

            # Convert the Row object to a dictionary
            if query_result:
                swm_policy_table_names = [column[0] for column in self.cursor.description]
                swmpolicy_query_result_dict = dict(zip(swm_policy_table_names, query_result))
            else:
                swmpolicy_query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            swmpolicy_query_result_dict = self.convert_datetimes_and_decimals(swmpolicy_query_result_dict)
            formatted_result = json.dumps(swmpolicy_query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of SWM Policies:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            SWMP_ID = result_dict.get("ID", None)
            SWMP_Name = result_dict.get("Name", None)
            SWMP_Level = result_dict.get("Level", None)
            SWMP_Version = result_dict.get("Version", None)
            SWMP_SourceFacility = result_dict.get("SourceFacility", None)
            SWMP_SourceWorkCenter = result_dict.get("SourceWorkCenter", None)
            SWMP_SourceDevice = result_dict.get("SourceDevice", None)
            SWMP_SourceTestProgram = result_dict.get("SourceTestProgram", None)
            SWMP_SourceProbes = result_dict.get("SourceProbes", None)
            SWMP_TargetFacility = result_dict.get("TargetFacility", None)
            SWMP_TargetWorkCenter = result_dict.get("TargetWorkCenter", None)
            SWMP_TargetDevice = result_dict.get("TargetDevice", None)
            SWMP_TargetTestProgram = result_dict.get("TargetTestProgram", None)
            SWMP_TargetProbes = result_dict.get("TargetProbes", None)
            SWMP_MergeFacility = result_dict.get("MergeFacility", None)
            SWMP_MergeWorkCenter = result_dict.get("MergeWorkCenter", None)
            SWMP_MergeDevice = result_dict.get("MergeDevice", None)
            SWMP_MergeTestProgram = result_dict.get("MergeTestProgram", None)
            SWMP_MergeProbes = result_dict.get("MergeProbes", None)
            SWMP_ProceedIfSWaferNotExist = result_dict.get("ProceedIfSWaferNotExist", None)
            SWMP_ProceedIFTWaferNotExist = result_dict.get("ProceedIFTWaferNotExist", None)
            SWMP_SWMDieTypeID = result_dict.get("SWMDieTypeID", None)
            SWMP_IgnoreTestTemperature = result_dict.get("IgnoreTestTemperature", None)
            SWMP_SourceDieTypes = result_dict.get("SourceDieTypes", None)
            SWMP_TargetDieTypes = result_dict.get("TargetDieTypes", None)
            SWMP_ParametricDataCopyID = result_dict.get("ParametricDataCopyID", None)

            # Compare fetched results with expected results
            comparison_results = {
                "ID": (SWMP_ID == expected_results["ID"]),
                "Name": (SWMP_Name == expected_results["Name"]),
                "Level": (SWMP_Level == expected_results["Level"]),
                "Version": (SWMP_Version == expected_results["Version"]),
                "SourceFacility": (SWMP_SourceFacility == expected_results["SourceFacility"]),
                "SourceWorkCenter": (SWMP_SourceWorkCenter == expected_results["SourceWorkCenter"]),
                "SourceDevice": (SWMP_SourceDevice == expected_results["SourceDevice"]),
                "SourceTestProgram": (SWMP_SourceTestProgram == expected_results["SourceTestProgram"]),
                "SourceProbes": (SWMP_SourceProbes == expected_results["SourceProbes"]),
                "TargetFacility": (SWMP_TargetFacility == expected_results["TargetFacility"]),
                "TargetWorkCenter": (SWMP_TargetWorkCenter == expected_results["TargetWorkCenter"]),
                "TargetDevice": (SWMP_TargetDevice == expected_results["TargetDevice"]),
                "TargetTestProgram": (SWMP_TargetTestProgram == expected_results["TargetTestProgram"]),
                "TargetProbes": (SWMP_TargetProbes == expected_results["TargetProbes"]),
                "MergeFacility": (SWMP_MergeFacility == expected_results["MergeFacility"]),
                "MergeWorkCenter": (SWMP_MergeWorkCenter == expected_results["MergeWorkCenter"]),
                "MergeDevice": (SWMP_MergeDevice == expected_results["MergeDevice"]),
                "MergeTestProgram": (SWMP_MergeTestProgram == expected_results["MergeTestProgram"]),
                "MergeProbes": (SWMP_MergeProbes == expected_results["MergeProbes"]),
                "ProceedIfSWaferNotExist": (
                            SWMP_ProceedIfSWaferNotExist == expected_results["ProceedIfSWaferNotExist"]),
                "ProceedIFTWaferNotExist": (
                            SWMP_ProceedIFTWaferNotExist == expected_results["ProceedIFTWaferNotExist"]),
                "SWMDieTypeID": (SWMP_SWMDieTypeID == expected_results["SWMDieTypeID"]),
                "IgnoreTestTemperature": (SWMP_IgnoreTestTemperature == expected_results["IgnoreTestTemperature"]),
                "SourceDieTypes": (SWMP_SourceDieTypes == expected_results["SourceDieTypes"]),
                "TargetDieTypes": (SWMP_TargetDieTypes == expected_results["TargetDieTypes"]),
                "ParametricDataCopyID": (SWMP_ParametricDataCopyID == expected_results["ParametricDataCopyID"]),
            }

            # Print and log the comparison results
            for key, match in comparison_results.items():
                if match:
                    self.logger.info(f"{key} matches expected value.")
                else:
                    self.logger.error(
                        f"{key} does NOT match expected value. Expected: {expected_results[key]}, Found: {result_dict.get(key)}")

            # Store the result in context if needed
            context.wafer_details_from_db = swmpolicy_query_result_dict
            self.logger.info(f"Query SWM Policies executed successfully with comparison results: {comparison_results}")

        except Exception as e:
            self.logger.error("Error in dataWaferTable: %s", e)
            MyException.handle_exception(context, e)

    def dataSwmAutomatedPolicies(self, context):
        try:
            # Define hardcoded expected results
            expected_results = {
                "ID": 1021,
                "PolicyID": 1018,
                "StatusID": 3,
                "IsAutomated": 0
            }

            # Query to retrieve data from Automated Policies
            query_result = self.cursor.execute("SELECT * FROM SWMAutomatedPolicies AS sp").fetchone()
            self.logger.info("Query Result of SWM Automated Policies: %s", query_result)
            self.logger.info("Query SWM Automated Policy executed successfully")

            context.user_details_from_db = query_result

            # Convert the Row object to a dictionary
            if query_result:
                swm_policy_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(swm_policy_table_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of SWM Automated Policies:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            ID = result_dict.get("ID", None)
            SWMAutomate_PolicyID = result_dict.get("PolicyID", None)
            SWMAutomate_Status = result_dict.get("StatusID", None)
            SWMAutomate_IsAutomated = result_dict.get("IsAutomated", None)

            # Compare fetched results with expected results
            comparison_results = {
                "ID": (ID == expected_results["ID"]),
                "PolicyID": (SWMAutomate_PolicyID == expected_results["PolicyID"]),
                "StatusID": (SWMAutomate_Status == expected_results["StatusID"]),
                "IsAutomated": (SWMAutomate_IsAutomated == expected_results["IsAutomated"]),
            }

            # Print and log the comparison results
            for key, match in comparison_results.items():
                if match:
                    self.logger.info(f"{key} matches expected value.")
                else:
                    self.logger.error(
                        f"{key} does NOT match expected value. Expected: {expected_results[key]}, Found: {result_dict.get(key)}")

            # Store the result in context if needed
            context.wafer_details_from_db = query_result_dict
            self.logger.info(f"Query SWM Automated Policies executed successfully with comparison results: {comparison_results}")

        except Exception as e:
            self.logger.error("Error in dataWaferTable: %s", e)
            MyException.handle_exception(context, e)

    def dataLotTableVerification(self, context):
        try:
            # Define hardcoded expected results
            expected_results = {
                "Lot_Sequence": 3111,
                "Lot_ID": "73631",
                "Program_Name": "PREBAKE_A_4670_POSTBAKE_A_4670",
                "Work_Center": "WAFER SORT_WAFER SORT",
                "Facility_ID": "WEB SMALL DATASET",
                "Sublot_ID": "1",
                "Part_Type": "4670"
            }

            # Query to fetch the Lot of Data from the database
            query_result = self.cursor.execute("SELECT * FROM lot AS l ORDER BY 1 DESC").fetchone()
            self.logger.info("Query Result of lot table: %s", query_result)

            # Store the result in the context if needed
            context.user_details_from_db = query_result
            context.details_from_db = query_result

            # Convert the Row object to a dictionary
            if query_result:
                lot_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(lot_table_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of Lot Table:\n%s", formatted_result)

            # Load the JSON string into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            Lot_Sequence_Primary = result_dict.get("Lot_Sequence", None)
            Lot_ID = result_dict.get("Lot_ID", None)
            Lot_Program_Name = result_dict.get("Program_Name", None)
            Lot_Work_Center = result_dict.get("Work_Center", None)
            Lot_Facility_ID = result_dict.get("Facility_ID", None)
            Lot_Sublot_ID = result_dict.get("Sublot_ID", None)
            Lot_Device_Name = result_dict.get("Part_Type", None)

            context.user_details_from_db = query_result_dict
            self.logger.info(
                f"Query Result of Lot Table is: {Lot_Sequence_Primary}, {Lot_ID}, {Lot_Program_Name}, {Lot_Work_Center}, {Lot_Facility_ID}, {Lot_Device_Name}, {Lot_Sublot_ID}")

            # Compare fetched results with expected results
            comparison_results = {
                "Lot_Sequence": (Lot_Sequence_Primary == expected_results["Lot_Sequence"]),
                "Lot_ID": (Lot_ID == expected_results["Lot_ID"]),
                "Program_Name": (Lot_Program_Name == expected_results["Program_Name"]),
                "Work_Center": (Lot_Work_Center == expected_results["Work_Center"]),
                "Facility_ID": (Lot_Facility_ID == expected_results["Facility_ID"]),
                "Sublot_ID": (Lot_Sublot_ID == expected_results["Sublot_ID"]),
                "Part_Type": (Lot_Device_Name == expected_results["Part_Type"])
            }

            # Print and log the comparison results
            for key, match in comparison_results.items():
                if match:
                    self.logger.info(f"{key} matches expected value.")
                else:
                    self.logger.error(
                        f"{key} does NOT match expected value. Expected: {expected_results[key]}, Found: {result_dict.get(key)}")

            # Store the result in context if needed
            context.wafer_details_from_db = query_result_dict
            self.logger.info(f"Query Lot Table executed successfully with comparison results: {comparison_results}")

        except Exception as e:
            self.logger.error("Error in dataWaferTable: %s", e)
            MyException.handle_exception(context, e)

    def dataTestParamMapVerification(self, context):
        try:
            # Define hardcoded expected results
            expected_results = {
                "Lot_Sequence": 4,
                "Test_Number": 0.0,
                "Test_Name": "0",
                "Column_Name": None,
                "Program_Name": "3616_TP",
                "Table_Name": "_3616_TP_001"
            }

            # Query to fetch the Data of Test Parameter Map from database
            query_result = self.cursor.execute("SELECT * FROM Test_Param_Map as tpm").fetchone()
            self.logger.info("Query Result of Test Param Map table: %s", query_result)

            # Convert the Row object to a dictionary
            if query_result:
                tpm_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(tpm_table_names, query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of Test Param Map:\n%s", formatted_result)

            # Load the JSON String into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            TPM_Lot_Sequence = result_dict.get("Lot_Sequence", None)
            TPM_Test_Number = result_dict.get("Test_Number", None)
            TPM_Test_Name = result_dict.get("Test_Name", None)
            TPM_Column_Name = result_dict.get("Column_Name", None)
            TPM_Program_Name = result_dict.get("Program_Name", None)
            TPM_Table_Name = result_dict.get("Table_Name", None)

            context.user_details_from_db = query_result_dict
            self.logger.info(
                f"Query Result of Test Param Map is {TPM_Lot_Sequence}, {TPM_Test_Number}, {TPM_Test_Name}, {TPM_Column_Name}, {TPM_Program_Name}, {TPM_Table_Name}")

            # Compare fetched results with expected results
            comparison_results = {
                "Lot_Sequence": (TPM_Lot_Sequence == expected_results["Lot_Sequence"]),
                "Test_Number": (TPM_Test_Number == expected_results["Test_Number"]),
                "Test_Name": (TPM_Test_Name == expected_results["Test_Name"]),
                "Column_Name": (TPM_Column_Name == expected_results["Column_Name"]),
                "Program_Name": (TPM_Program_Name == expected_results["Program_Name"]),
                "Table_Name": (TPM_Table_Name == expected_results["Table_Name"])
            }

            # Print and log the comparison results
            for key, match in comparison_results.items():
                if match:
                    self.logger.info(f"{key} matches expected value.")
                else:
                    self.logger.error(
                        f"{key} does NOT match expected value. Expected: {expected_results[key]}, Found: {result_dict.get(key)}")

            # Store the result in context if needed
            context.test_param_map_details_from_db = query_result_dict
            self.logger.info(
                f"Query Test Param Map executed successfully with comparison results: {comparison_results}")

        except Exception as e:
            self.logger.error("Error in dataTestParamMapVerification: %s", e)
            MyException.handle_exception(context, e)

    def dataSwmDashboardVerification(self, context):
        try:
            # Define hardcoded expected results
            expected_results = {
                "ID": 2041,
                "PolicyID": 2019,
                "StatusID": 4,
                "SourceFacility": "SILICON 6607",
                "SourceWorkCenter": "WAFER SORT",
                "SourceDevice": "4670"
            }
            # Query to fetch the Lot Data from database
            swmdashboard_query_result = self.cursor.execute("SELECT * FROM swmDashboard AS sDashboard").fetchone()
            self.logger.info("Query Result of Swm Dashboard table: %s", swmdashboard_query_result)

            # Convert the Row object to a dictionary
            if swmdashboard_query_result:
                swmdashboard_table_names = [column[0] for column in self.cursor.description]
                query_result_dict = dict(zip(swmdashboard_table_names, swmdashboard_query_result))
            else:
                query_result_dict = None

            # Convert JSON, datetime and Decimal objects to strings
            query_result_dict = self.convert_datetimes_and_decimals(query_result_dict)
            formatted_result = json.dumps(query_result_dict, indent=4, default=str)
            self.logger.info("Query Result of SWM Dashboard Verification:\n%s", formatted_result)

            # Load the JSON String into a dictionary
            result_dict = json.loads(formatted_result)

            # Access custom values from the dictionary using keys
            swmdashboard_ID = result_dict.get("ID", None)
            swmdashboard_PolicyID = result_dict.get("PolicyID", None)
            swmdashboard_StatusID = result_dict.get("StatusID", None)
            swmdashboard_SourceFacility = result_dict.get("SourceFacility", None)
            swmdashboard_SourceWorkCenter = result_dict.get("SourceWorkCenter", None)
            swmdashboard_SourceDevice = result_dict.get("SourceDevice", None)

            context.user_details_from_db = query_result_dict
            self.logger.info(
                f"Query Swm Dashboard of Test Param Map is {swmdashboard_ID}, {swmdashboard_PolicyID}, {swmdashboard_StatusID}, {swmdashboard_SourceFacility}, {swmdashboard_SourceWorkCenter}, {swmdashboard_SourceDevice}")

            # Compare fetched results with expected results
            comparison_results = {
                "ID": (swmdashboard_ID == expected_results["ID"]),
                "PolicyID": (swmdashboard_PolicyID == expected_results["PolicyID"]),
                "Test_Name": (swmdashboard_StatusID == expected_results["StatusID"]),
                "SourceFacility": (swmdashboard_SourceFacility == expected_results["SourceFacility"]),
                "SourceWorkCenter": (swmdashboard_SourceWorkCenter == expected_results["SourceWorkCenter"]),
                "SourceDevice": (swmdashboard_SourceDevice == expected_results["SourceDevice"])
            }

            # Print and log the comparison results
            for key, match in comparison_results.items():
                if match:
                    self.logger.info(f"{key} matches expected value.")
                else:
                    self.logger.error(
                        f"{key} does NOT match expected value. Expected: {expected_results[key]}, Found: {result_dict.get(key)}")

            # Store the result in context if needed
            context.test_param_map_details_from_db = query_result_dict
            self.logger.info(
                f"Query Test Param Map executed successfully with comparison results: {comparison_results}")

        except Exception as e:
            self.logger.error("Error in dataTestParamMapVerification: %s", e)
            MyException.handle_exception(context, e)

    def convert_datetimes_and_decimals(self, data):
        if isinstance(data, dict):
            return {key: self.convert_datetimes_and_decimals(value) for key, value in data.items()}
        elif isinstance(data, (list, tuple)):
            return [self.convert_datetimes_and_decimals(item) for item in data]
        elif isinstance(data, datetime):
            return str(data)
        elif isinstance(data, Decimal):
            return float(data)
        else:
            return data
