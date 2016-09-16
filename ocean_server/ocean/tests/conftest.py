"""
conftest.py module for ocean
"""

# Standard library imports
import configparser
import logging
import os
import os.path as path
import shutil
import subprocess as sp
import time
import uuid

# Third party imports
import pytest

# Local imports
import ocean.constants as oc
import ocean.tests.constants as tc


log = logging.getLogger(__name__)


CONFTEST_DIR = path.dirname(path.realpath(__file__))
DATA_DIR = path.join(CONFTEST_DIR, tc.PG_DATA_DIR)


def source_test_environ():
    """Source the test environment"""
    log.debug('source_test_environ()')
    root_dir = path.dirname(path.realpath(oc.__file__))
    config_path = path.abspath(path.join(root_dir, oc.ENVIRONMENT_PATH))
    parser = configparser.ConfigParser()
    parser.read(config_path)
    for k, v in parser['dev'].items():
        os.environ[k] = v


def start_db_server():
    """Spin up a test database server"""
    log.debug('start_db_server()')
    try:
        os.mkdir(DATA_DIR)
    except FileExistsError:
        shutil.rmtree(DATA_DIR)
    sp.check_call(['initdb', '-D', DATA_DIR])
    db_proc = sp.Popen(['postgres', '-D', DATA_DIR])
    time.sleep(0.5)  # Ensure the db has time to start
    return db_proc


def create_test_db():
    """Create a test database with a unique name"""
    log.debug('create_test_db()')
    db_name = 'ocean_test_' + str(uuid.uuid1())
    log.debug('db_name: %s', db_name)
    sp.check_call(['createdb', db_name])
    return db_name


def teardown_db(db_name):
    """Teardown the test database"""
    sp.check_call(['dropdb', db_name])


@pytest.yield_fixture(autouse='true', scope='session')
def test_db():
    """Instantiate a test database"""
    source_test_environ()
    db_proc = start_db_server()
    db_name = create_test_db()
    yield db_name
    try:
        teardown_db(db_name)
    finally:
        db_proc.terminate()
    try:
        shutil.rmtree(DATA_DIR)
    except FileNotFoundError:
        pass
