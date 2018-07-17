# pylint: skip-file
import os
import json

def test_rmd_header(script_runner, tmpdir):    
    ret = script_runner.run('python3', 'o2rmeta.py', '-debug', 'extract', 
        '-i', 'extract/tests/licenses/rmd',
        '-o', str(tmpdir),
        '-xo', '-m')
    print(ret.stdout)
    print(ret.stderr)

    assert ret.success, "process should return success"
    assert ret.stderr == '', "stderr should be empty"
    
    metadata = json.load(open(os.path.join(str(tmpdir), 'metadata_raw.json')))
    assert "title" in metadata, "should have title entry"
    assert "container ships" in metadata['title']
    assert "license" in metadata, "should have license entry"
    assert len(metadata['license']) == 5, "should have 5 licenses"
    assert metadata['license']['code'] == "Apache-2.0"
    assert metadata['license']['data'] == "CC0-1.0"
    assert metadata['license']['text'] == "ODbL-1.0"
    assert metadata['license']['ui_bindings'] == "good boy license"
    assert metadata['license']['metadata'] == "license-md.txt"

def test_rmd_header_incomplete(script_runner, tmpdir):    
    ret = script_runner.run('python3', 'o2rmeta.py', '-debug', 'extract', 
        '-i', 'extract/tests/licenses/rmd_incomplete',
        '-o', str(tmpdir),
        '-xo', '-m')
    print(ret.stdout)
    print(ret.stderr)

    assert ret.success, "process should return success"
    assert ret.stderr == '', "stderr should be empty"
    
    metadata = json.load(open(os.path.join(str(tmpdir), 'metadata_raw.json')))
    assert "license" in metadata, "should have license entry"
    assert len(metadata['license']) == 2, "should have only 2 license"
    assert "data" not in metadata['license'], "should not have license entry for data"
    assert "ui_bindings" not in metadata['license'], "should not have license entry for ui_bindings"
    assert "text" not in metadata['license'], "should not have license entry for text"
    assert metadata['license']['code'] == "Apache-2.0"
    assert metadata['license']['metadata'] == "CC0-1.0"

def test_erc_yml(script_runner, tmpdir):
    ret = script_runner.run('python3', 'o2rmeta.py', '-debug', 'extract', 
        '-i', 'extract/tests/licenses/erc_yml',
        '-o', str(tmpdir),
        '-xo', '-m')
    print(ret.stdout)
    print(ret.stderr)

    assert ret.success, "process should return success"
    assert ret.stderr == '', "stderr should be empty"
    
    metadata = json.load(open(os.path.join(str(tmpdir), 'metadata_raw.json')))
    assert "license" in metadata, "should have license entry"
    assert len(metadata['license']) == 5, "should have 5 licenses"
    assert metadata['license']['code'] == "Apache-2.0"
    assert metadata['license']['data'] == "ODbL-1.0"
    assert metadata['license']['text'] == "CC0-1.0"
    assert metadata['license']['ui_bindings'] == "proprietary license"
    assert metadata['license']['metadata'] == "license-md.txt"