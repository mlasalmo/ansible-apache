#!/usr/bin/env python
"""
testing molecule
"""

import os
import pytest

import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('ubuntu18')


@pytest.mark.parametrize('pkg', [
    'apache2',
    'ufw'
])
def test_pkg(host, pkg):
    """
    test packages
    """
    package = host.package(pkg)

    assert package.is_installed


@pytest.mark.parametrize('svc', [
    'apache2',
    'ufw'
])
def test_svc(host, svc):
    """
    test services
    """
    service = host.service(svc)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize('rule', [
    '-A ufw-user-input -p tcp -m tcp --dport 80 -j ACCEPT'
])
def test_ufw_rules(host, rule):
    """
    test firewall
    """
    cmd = host.run('iptables -t filter -S')

    assert rule in cmd.stdout
