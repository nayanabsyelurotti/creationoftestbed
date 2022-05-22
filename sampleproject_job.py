'''
sampleproject_job.py
'''
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2019, Cisco Systems Inc.'
__contact__ = ['pyats-support-ext@cisco.com']
__credits__ = ['list', 'of', 'credit']
__version__ = 1.0

import os
from genie.harness.main import gRun
from pyats.easypy import run


def main():
    '''job file entrypoint'''
    
    gRun(
    	pdb = False,
    	trigger_datafile = "sampleproject_data.yaml",
    	trigger_uids = ["TriggerCommonSetup","TriggerGetRunningConfig","TriggerCommonCleanup"]
    )
    
