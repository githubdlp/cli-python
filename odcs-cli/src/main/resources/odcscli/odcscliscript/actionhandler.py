#!/usr/bin/env python

import configparser as ConfigParser
import io
import json
import os
import platform
import re
import logging
from collections import OrderedDict

try:
    from messages import Messages, ErrorMessages
except:
    from .messages import Messages, ErrorMessages


logger = logging.getLogger(__name__)

#=== CLASSES ==================================================================

class ActionHandler(object):
        
    def handleCreate(self, args):
        print("inside Create Action Handler {}".format(args.name))
        return 
    
    def handlePush(self, args):
        print("inside Push Action Handler {}".format(args.name))
        return  
    
    def handleConfigLogLevel(self, args):
        sys.stdout.write(Messages.ODCS_CLI_INFO_LOG_LEVEL_UPDATE_MSG % args.loglevel)  
