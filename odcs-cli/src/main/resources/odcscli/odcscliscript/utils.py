#!/usr/bin/env python

import configparser as ConfigParser
import io
import json
import os
import platform
import re
import logging
from collections import OrderedDict


#=== CLASSES ==================================================================

class OdcsConfigParser(ConfigParser.RawConfigParser):
    """
    based on ConfigParser from the standard library, modified to parse config
    files without sections.
    """
    
    def read(self, filename):
        text = open(filename).read()
        f = io.StringIO("[%s]\n" % NOSECTION + text)
        self.read_file(f, filename)
        
    def write(self, fp):
        """
        overriding the default configparser to fit the need without section.
        Write the items from the default section manually and then remove them
        from the data. They'll be re-added later.
        """
        try:
            default_section_items = self.items(NOSECTION)
            self.remove_section(NOSECTION)

            for (key, value) in default_section_items:
                fp.write("{0} = {1}\n".format(key, value))

            # fp.write("\n")
        except ConfigParser.NoSectionError:
            pass

        ConfigParser.RawConfigParser.write(self, fp)
        self.add_section(NOSECTION)
        for (key, value) in default_section_items:
            self.set(NOSECTION, key, value)
    
    def getoptionslist(self):
        'get a list of available options'
        return self.options(NOSECTION)
            
    def getoption(self, option):
        'get the value of an option'
        return self.get(NOSECTION, option)
    
    def hasoption(self, option):
        """
        return True if an option is available, False otherwise.
        (NOTE: do not confuse with the original has_option)
        """
        return self.has_option(NOSECTION, option)
    
    
    
    
    

class Utils(object):
    
    def __init__(self):
        self._odcsConfigParser = OdcsConfigParser()
        usrHome = os.path.expanduser('~')
        
        self.odcsDir = usrHome + "/.odcs"
        self.odcs_log_dir_name = 'log'
        self.odcs_log_dir = self.odcsDir + "/" + self.odcs_log_dir_name
        self.logFile = "/odcscli.log"
        
        # configuration file
        self.odcs_conf_dir_name = 'conf'
        self._confFile = "/" + self.odcs_conf_dir_name + "/setup.conf"
        self._default_log_level = INFO

        # parameter key in the conf file
        self._log_level = 'logLevel'
                
    @property 
    def log_file_name(self):
        # concatenate to give the full path as a string.
        return self.odcs_log_dir + self.logFile
    
    @property 
    def log_level(self):
        return self._log_level
    
    @property 
    def default_log_level(self):
        return self._default_log_level
    
    @property 
    def conf_file_name(self):
        # concatenate to give the full path as a string.
        return self.odcsDir + self._confFile
    
    def readConfigFile(self):
        # import configreader
        ocp = self._odcsConfigParser
        if os.path.exists(self.conf_file_name):
            ocp.read(self.conf_file_name)
            return ocp;
        else:
            return None
        
    def writeValueToConfigFile(self, key, value):
        # write the value to the config file. either adds a value
        # if not present or overrides the current value.
        ocp = self._odcsConfigParser
        ocp.set(NOSECTION, key, value)
        with open(self.conf_file_name, 'w') as configfile:
              ocp.write(configfile)
        




#=== MODULE METHODS ================================================================

def get_log_filename():
    utils = Utils()
    if not os.path.exists(utils.odcsDir):
        os.makedirs(utils.odcsDir)
    if not os.path.exists(utils.odcs_log_dir):
        os.makedirs(utils.odcs_log_dir)
    
    return utils.log_file_name

def get_log_level():
    utils = Utils()
    ocp = utils.readConfigFile()
    if ocp and utils.log_level.lower() in ocp.getoptionslist():
        # return the log level in upper case for configuration.
        return ocp.getoption(utils.log_level.lower()).upper()
    else:
        return utils.default_log_level
    
#=== CONSTANTS ================================================================

logger = logging.getLogger(__name__)

# LOG LEVEL CONSTANTS
INFO = 'INFO'
DEBUG = 'DEBUG'
ERROR = 'ERROR'
CRITICAL = 'CRITICAL'
WARNING = 'WARNING'

# section name for options without section:
NOSECTION = 'NOSECTION'

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(module)s: %(message)s',
            'datefmt': '%b %d %H:%M:%S'
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'filename': get_log_filename(),
            'maxBytes': 10485760,
            'backupCount': 10,
            'encoding': 'utf8'
        },
    },
    'loggers': {
        '': {                  
            'handlers': ['default'],
            'level': get_log_level(),
            'propagate': True  
        }
    }
}
