******************************************************
ODCS
******************************************************

Prerequisite
*************
Python 3.3+

    .. code-block :: c
        
        # Verify Python 3.3+
        $ python ?-version
        Python 3.4.3

PSM Client Installation
***********************

    .. code-block :: c
    
        $ sudo -H pip/pip3 install -U odcscli-version.zip

It does following -

 - Install missing Python package dependencies (if any) from *requests*, *colorama* and *keyring*.
 - Download and install odcs client.
 - Create a symlink */bin/odcs* to the main executable.

ODCS Client Setup
****************
Before using odcs client, complete the setup using *odcs setup* command.
