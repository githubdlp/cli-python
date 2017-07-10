import os
import sys
from collections import OrderedDict


#################################################
######## Description and help Messages ##########
#################################################
class Messages(object):
    # Space is required after the script name. 
    ODCS_CLI_TOP_LEVEL_SCRIPT_NAME = "odcs "
    ODCS_CLI_USAGE = "odcs <command> [parameters]"
    ODCS_CLI_DESCRIPTION = 'A command line tool to interact with ODCS'
    ODCS_CLI_HELP_DESC = 'Show help'
    # version
    ODCS_CLI_VERSION_HELP_DESC = 'Show current version of odcs client'
    ODCS_CLI_VERISON_DISPLAY_MSG = 'ODCS CLI Client - version '
    # setup
    ODCS_CLI_SETUP_DESC = 'Configure odcs client options'    
    # Update
    ODCS_CLI_UPGRADE_DESC = 'Update odcs client to latest version'
    # log-level-description
    ODCS_CLI_LOG_LEVEL_DESC = 'View or update odcs client log level'
    # output format description
    ODCS_CLI_OUTPUT_FORMAT_HELP_DESC = 'Desired output format. Valid values are %s'
    # Tear down description
    ODCS_CLI_TEAR_DOWN_DESC = "Remove configured odcs client options"
    
    # Keys for parsing
    ODCS_CLI_SETUP_KEY = 'setup'
    ODCS_CLI_UPGRADE_KEY = 'update'
    ODCS_CLI_LOG_LEVEL = 'log'
    ODCS_CLI_TEAR_DOWN_KEY = 'cleanup'
    # Used for multiple purposes. Check bfr changing this value.
    ODCS_CLI_HELP_KEY = 'help'
    
    ODCS_CLI_JSON_KEY = 'json'
    ODCS_CLI_TEXT_KEY = 'text'
    ODCS_CLI_RETYPE_PWD = 'Retype %s: '
    
    # Keys for Help display
    ODCS_CLI_HELP_DESCRIPTION = 'DESCRIPTION'
    ODCS_CLI_HELP_SYNOPSIS = 'SYNOPSIS'
    ODCS_CLI_HELP_SERVICES = 'AVAILABLE SERVICES'
    ODCS_CLI_HELP_COMMANDS = 'AVAILABLE COMMANDS'
    ODCS_CLI_HELP_PARAMETERS = 'AVAILABLE PARAMETERS'
    ODCS_CLI_HELP_EXAMPLES = 'EXAMPLES'
    ODCS_CLI_HELP_PAYLOAD = 'SAMPLE PAYLOAD'
    
    
    # for argparse display arguments headers
    ODCS_CLI_RENAME_POSITIONAL_ARG = 'Available services'
    ODCS_CLI_RENAME_OPTIONAL_ARG = 'Optional arguments'
    
    # General Display Messages
    ODCS_CLI_WARNING_MSG = "WARNING"
    ODCS_CLI_INFO_MSG = 'INFO'
    #ODCS_CLI_JOB_STATUS_ID_MSG = 'Job ID : %s. Please use view-operation-status command to view details.\n'
    ODCS_CLI_JOB_STATUS_ID_MSG = 'Job ID : %s\n'
    ODCS_CLI_UPGRADE_WARNING_MSG = "A new version of odcs client is available. Please run 'odcs update' to update to the latest version."
    ODCS_CLI_SETUP_SUCCESS_MSG = "'odcs setup' was successful. Available services are:\n\n"
    ODCS_CLI_HELP_SAMPLE_PAYLOAD = "Required properties are indicated as \"required\". Replace in the actual payload with real values.\n"
    
    # configure msgs
    ODCS_CLI_WARN_OUTPUT_FORMAT_MSG = "\nWarning: Invalid output format. Valid values are %s. Defaulting to 'json'." 
    ODCS_CLI_WARN_LOG_LEVEL_MSG = "Warning: Invalid log level. Valid values are %s\n"
    ODCS_CLI_WARN_TEARDOWN_FORCE_MSG = "Warning: Invalid force value. Valid values are %s\n"
    ODCS_CLI_INFO_LOG_LEVEL_UPDATE_MSG = "Successfully updated the log level to '%s'\n"
    ODCS_CLI_INFO_CURRENT_LOG_LEVEL_MSG = "Current log level is '%s'\n"
    ODCS_CLI_TEAR_DOWN_PROMT_MSG = "All configuration and data created by 'odcs setup' will be removed.\nProceed (y/n)? "
    ODCS_CLI_TEAR_DOWN_RESPONE_MSG = "Your response ('{0}') was not one of the expected responses: {1}\n"
    ODCS_CLI_TEAR_DOWN_SUCCESS_MSG = "Cleanup successful"
    ODCS_CLI_TEAR_DOWN_SUCCESS_DISPLAY = ODCS_CLI_TEAR_DOWN_SUCCESS_MSG + ". To use the odcs client again, configure it using 'odcs setup'.\n"
    
    # General Logger Info Msgs
    ODCS_CLI_CHK_CONN = "Checking connection authorization"
    ODCS_CLI_DOWNLOAD_CATALOG = "Downloading the catalogs"
    ODCS_CLI_DOWNLOAD_CATALOG_SUCCESS = "Successfully downloaded catalog"
    ODCS_CLI_DOWNLOAD_KIT = "Downloading the latest kit"
    ODCS_CLI_DOWNLOAD_KIT_SUCCESS = "Successfully Downloaded the latest odcs client zip"
    ODCS_CLI_UPGRADE_LOG_SUCCESS = "Successfully updated the odcs client" 
    ODCS_CLI_LATEST_VERSION_EXISTS = 'You already have the most up-to-date version of odcs client installed on the system'
    ODCS_CLI_UPGRADE_DOWNLOAD_KIT = "...Downloading the latest odcs client distribution - version %s\n"
    ODCS_CLI_UPGRADE_DOWNLOAD_KIT_UPGRADING = "...Updating odcs client from version %s to %s\n"
    ODCS_CLI_UPGRADE_SUDO_PROMPT = "...If prompted for password, enter sudo password\n"
    ODCS_CLI_UPGRADE_CLEANING_UP = "...Cleaning up\n"
    ODCS_CLI_REMOVE_DIR_SUCCESS = "Successfully deleted {0} directory."
    ODCS_CLI_REMOVE_DIR_FAILURE = "Failed to delete the {0} directory: {1}."
    
    # Display msgs for custom commands.
    ODCS_CLI_LONG_CMD_EXEC_INFO_MSG = "This command might take a while to complete...\n"
    
    # Deprecated msgs for commands.
    ODCS_CLI_DEPRECATED = 'deprecated'
    ODCS_CLI_PARAM_DEPRECATED_INFO = "Warning: parameter '%s' is deprecated"
    ODCS_CLI_USE_PARAM_IF_DEPRECATED_INFO = "Use parameter '%s' instead."

#################################################
############### Error Messages ##################
#################################################
class ErrorMessages(object):
    # generic Error display msg
    ODCS_CLI_LOGGER_ERROR_MSG = 'Error: %s'
    ODCS_CLI_STD_ERR_MSG = 'Error: %s\n'
    
    ODCS_CLI_KEYBOARD_INTERRUPT = "Initiated KeyBoardInterrupt"
    
    # Logger msgs.
    ODCS_CLI_NO_DATA_FOUND = 'No data found'
    ODCS_CLI_FILE_NOT_FOUND = 'File Not Found Error: %s'
    ODCS_CLI_CONNECTION_ERROR = "Connection Error: %s"
    ODCS_CLI_TIMEOUT_ERROR = "Timeout: %s"
    ODCS_CLI_INVALID_URL_ERROR = "Invalid URL: %s"
    ODCS_CLI_REQUESTS_ERROR = "Request Exception: %s"
    ODCS_CLI_DOWNLOAD_KIT_ERROR = "Error while downloading the kit. with response code: %s"
    ODCS_CLI_UPGRADE_UNKNOWN_ARGS_ERROR = "%s unknown arguments for odcs update."
    ODCS_CLI_UPGRADE_LOG_ERROR = "Exception while updating the odcs client. KeyBoardInterrupt/CommandError"
    ODCS_CLI_UPGRADE_LOG_UNKOWN_ERROR = "Unknown error while updating the odcs client."
    ODCS_CLI_UPGRADE_LOG_BUILD_ERROR = "Previous build dir error."
    ODCS_CLI_UPGRADE_PIP_RETRY_ERROR = "Exception while updating using pip: %s. Retrying update using pip3"
    ODCS_CLI_UPGRADE_PIP_ERROR = "Exception while updating using pip: %s"
    ODCS_CLI_NO_VERSION_FOUND_ERROR ='No client and catalog version found in the response.'
    ODCS_CLI_UPGRADE_GENERIC_ERROR = "Response code: %s while trying to update the cli."
    ODCS_CLI_UPGRADE_DOWNLOAD_KIT_LOCATION_ERROR = "The downloaded file location path is None."
    ODCS_CLI_LOG_LEVEL_ERROR = "Please check the help by running 'odcs log h'.\n"
    ODCS_CLI_CONFIG_FILE_READ_ERROR = "Error while reading value from config file: %s"
    ODCS_CLI_TEAR_DOWN_CRED_ERROR = "Error while removing credentials: {0}"
    
    ODCS_CLI_CHK_CONN_FAIL_ERROR = "Check connection failed with status code: %s"
    ODCS_CLI_BAD_RESPONSE_ZIPFILE = "Bad Response: catalog zip file corrupted"
    
    # Configure Error Msgs
    ODCS_CLI_PWD_MATCH_ERROR_DISPLAY = 'Passwords do not match. Try again.'
    ODCS_CLI_FIELD_EMPTY_ERROR_DISPLAY = "'%s' can not be empty."
    ODCS_CLI_DEFAULT_URI_ERROR_DISPLAY = "Please re-configure the default Uri, by running 'odcs setup'."
    ODCS_CLI_INVALID_IDENTITY_DOMAIN_ERR_DISPLAY = "No valid account or subscription for domain %s. Please re-run 'odcs setup' and provide valid value for '%s'."
    ODCS_CLI_OUTPUT_FORMAT_ERROR_MSG = "Invalid output format. Valid values are %s. Please re-enter valid value for '%s'"
    ODCS_CLI_DNS_ERROR_DISPLAY = "DNS host name resolution failed for %s. Please re-run 'odcs setup' and provide fully qualified host name for '%s'."
    ODCS_CLI_UNAME_PWD_ERR_DISPLAY = "Username, Password and/or Identity domain are incorrect. Please re-enter."
    ODCS_CLI_REGION_ERR_DISPLAY = "Invalid region. Valid values are %s. Please re-enter valid value for '%s'."
    ODCS_CLI_GENERIC_SETUP_ERR_DISPLAY = "Please check values for '%s', '%s', '%s' and '%s', and re-run 'odcs setup'."
    ODCS_CLI_GENERIC_ERR_DISPLAY = "Setup failed. " + ODCS_CLI_GENERIC_SETUP_ERR_DISPLAY
    ODCS_CLI_GENERIC_SETUP_VALUES_ERR_DISPLAY = "Failed to establish connection. " + ODCS_CLI_GENERIC_SETUP_ERR_DISPLAY
    ODCS_CLI_UPGRADE_HELP_ERROR = 'Update help does not exist.'
    ODCS_CLI_UPGRADE_GENERIC_DISPLAY = "Please run 'odcs update' to update to the latest odcs client distribution."
    ODCS_CLI_SETUP_HELP_ERROR = 'Setup help does not exist.'
    ODCS_CLI_SETUP_GENERIC_DISPLAY = "Please run 'odcs setup' to configure odcs client."
    ODCS_CLI_TEARDOWN_HELP_ERROR = 'Cleanup help does not exist.'
    ODCS_CLI_LOG_LEVEL_HELP_ERROR = 'Log help does not exist.'
    ODCS_CLI_LOG_LEVEL_GENERIC_DISPLAY = "Please run 'odcs log --level <level>' to update the log level.\n"
    ODCS_CLI_UPGRADE_PIP_NOT_FOUND_ERROR = 'sudo: pip: command not found\n'
    ODCS_CLI_UPGRADE_DNS_ERROR_DISPLAY = "DNS host name resolution failed for defaultURI '%s'. Please provide fully qualified host name and re-run 'odcs setup'.\n"
    ODCS_CLI_UPGRADE_FAILED_ERR_DISPLAY = 'Update failed.\n'    
     
    # Display error messages
    ODCS_CLI_FAIL_JOB_ID = "Failed to get the Job Id: %s"
    ODCS_CLI_CONNECTION_ERROR_DISPLAY = "Failed to connect to the server. %s"
    ODCS_CLI_TIMEOUT_ERROR_DISPLAY = "Request timed out. %s"
    ODCS_CLI_INVALID_URL_ERROR_DISPLAY = "Malformed URL. %s"
    ODCS_CLI_CONFIG_CORRUPTED = "odcs client configuration corrupted. Please re-run 'odcs setup'.\n"
    ODCS_CLI_STATUS_CODE_ERROR_DISPLAY = 'Status: %s Problem with the request. Exiting.\n'
    ODCS_CLI_BAD_RESPONSE_ZIPFILE_DISPLAY = "odcs setup failed while trying to download the catalog.\n"
    ODCS_CLI_DOWNLOAD_KIT_CORRUPTED_DISPLAY = "Downloaded file corrupted. Exiting the odcs update.\n"
    ODCS_CLI_SHORT_OUTPUT_PARSING_ERROR_DISPLAY = "Exception while trying to format output for short format: {}"
    
    # Custom Command Error Msgs
    ODCS_CLI_SPECIFY_ONE_ARGUMENT_ERROR = "specify only one of these parameters {}"
    ODCS_CLI_NO_SUCH_FILE_EXISTS_ERROR = "argument {0}: can't open '{1}': No such file or directory: '{1}'"
    ODCS_CLI_MAX_LIMIT_ERROR = "argument {0}: the max limit to upload the application is {1}: Failed to upload application '{2}'"
