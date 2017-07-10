#!/usr/bin/env python

import argparse
import sys
import logging.config
from collections import OrderedDict
try:
    from utils import Utils, LOGGING_CONFIG
    from actionhandler import ActionHandler
except:
    from .utils import Utils, LOGGING_CONFIG
    from .actionhandler import ActionHandler
    
    
logger = logging.getLogger(__name__)

def main():
    OdcsCommandParser()
    
class OdcsCommandParser(object):
    
    Utils()
    actionHandler = ActionHandler()
    logging.config.dictConfig(LOGGING_CONFIG)

    def __init__(self):
        parser = argparse.ArgumentParser(description='Try odcs <COMMAND> --help for specific details',
                                         usage='''odcs <COMMAND> [<args>]
                                         
    The most commonly used odcs COMMANDs are:
    create        create an app 
    push          push the code to the app
    logs          shows the logs  
    ps            process status
    config        configure the CLI
                ''')
        parser.add_argument('command', help='command to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print ("Unrecognized COMMAND")
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def create(self):
        parser = argparse.ArgumentParser(description='Create an app', usage='''odcs create [<args>]''')
        parser.add_argument('--name', help='name of the app')
        args = parser.parse_args(sys.argv[2:])
        logger.info("Invoking action handler for create command with arg %s" % args)
        self.actionHandler.handleCreate(args)

    def push(self):
        parser = argparse.ArgumentParser(description='Push the code to the app', usage='''odcs push [<args>]''')
        parser.add_argument('name', help='name of the app')
        args = parser.parse_args(sys.argv[2:])
        logger.info("Invoking action handler for push command with arg %s" % args)
        self.actionHandler.handlePush(args)
        
    def config(self):
        parser = argparse.ArgumentParser(description='Configure the CLI option', usage='''odcs config <OPTION> [<args>]
        
    Available OPTIONs are
    loglevel        set the loglevel for CLI logging
        ''')
        parser.add_argument('option', help='option to run')
        args = parser.parse_args(sys.argv[2:3])
        logger.debug("config command invoked with argument {}".format(args))
        if not hasattr(self, "option_" + args.option):
            print ("Unrecognized OPTION")
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, "option_" + args.option)()
        
    def option_loglevel(self):
        parser = argparse.ArgumentParser(description='Set the loglevel for CLI logging', usage='''odcs config loglevel <LOG_LEVEL>''')
        parser.add_argument('loglevel', help='loglevel to be set. valid values are [DEBUG, INFO, WARNING, ERROR, CRITICAL]')
        args = parser.parse_args(sys.argv[3:])
        logger.info("Invoking action handler for config loglevel with arg %s" % args)
        self.actionHandler.handleConfigLogLevel(args)
            
if __name__ == "__main__":
    OdcsCommandParser()
