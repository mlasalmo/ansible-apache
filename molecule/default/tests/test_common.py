#!/usr/bin/env python
"""
testing molecule
"""

import os
import pytest

import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('file, content', [
    ("/var/www/html/index.html", "Managed by Ansible")
])
def test_files(host, file, content):
    """
    test_files
    """
    file = host.file(file)

    assert file.exists
    assert file.contains(content)
