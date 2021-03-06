#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
#   Filename:  test_arclink_waveforms.py
#   Author:    Kasra Hosseini
#   Email:     kasra.hosseinizad@earth.ox.ac.uk
#   License:   GPLv3
# -------------------------------------------------------------------

# -----------------------------------------------------------------------
# ----------------Import required Modules (Python and Obspy)-------------
# -----------------------------------------------------------------------

# Required Python and Obspy modules will be imported in this part.
from obspyDMT.utils.input_handler import command_parse, read_input_command

# ##################### test_arclink_waveforms ###############################


def test_arclink_waveforms():
    (options, args, parser) = command_parse()
    input_dics = read_input_command(parser)

    import os
    input_dics['datapath'] = os.path.join(os.path.curdir, 'event_based_dir_ARCLINK')
    input_dics['min_date'] = '2014-01-01'
    input_dics['max_date'] = '2015-01-01'
    input_dics['min_mag'] = '7.9'
    input_dics['identity'] = 'II.*.00.BHZ'
    input_dics['event_catalog'] = 'NEIC_USGS'
    input_dics['data_source'] = ['ARCLINK']
    input_dics['req_parallel'] = True
    input_dics['instrument_correction'] = True
    input_dics['net'] = 'II'
    input_dics['sta'] = '*'
    input_dics['loc'] = '00'
    input_dics['cha'] = 'BHZ'
    input_dics['offset'] = 100

    from obspyDMT import obspyDMT
    input_dics = obspyDMT.dmt_core(input_dics)

    from glob import glob
    assert len(glob(os.path.join(os.path.curdir, 'event_based_dir_ARCLINK', '*'))) == 3
    # uncomment the following lines
    #assert len(glob(os.path.join(os.path.curdir, 'event_based_dir_ARCLINK', '20140401_234647.a', '*'))) == 4
    #assert len(glob(os.path.join(os.path.curdir, 'event_based_dir_ARCLINK', '20140623_205309.a', '*'))) == 4
    #assert len(glob(os.path.join(os.path.curdir, 'event_based_dir_ARCLINK', '20140401_234647.a', 'raw', '*'))) >= 5
    #assert len(glob(os.path.join(os.path.curdir, 'event_based_dir_ARCLINK', '20140623_205309.a', 'raw', '*'))) >= 5
    #assert len(glob(os.path.join(os.path.curdir, 'event_based_dir_ARCLINK', '20140401_234647.a', 'processed', '*'))) >= 5
    #assert len(glob(os.path.join(os.path.curdir, 'event_based_dir_ARCLINK', '20140623_205309.a', 'processed', '*'))) >= 5

    import shutil
    shutil.rmtree(os.path.join(os.path.curdir, 'event_based_dir_ARCLINK'))
    shutil.rmtree('./obspydmt-data')
