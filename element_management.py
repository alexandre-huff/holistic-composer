#!/usr/bin/env python

import requests
from utils import *


class ElementManagement:
    """Implementation of the Click-on-OSv Element Management (EM)."""

    def __init__(self):
        self.header = {'Content-Type': 'application/json'}

    def get_version(self, vnf_ip):
        """Return Click version."""

        url = create_url(vnf_ip, 'version')
        payload = {'op': 'GET'}
        return requests.get(url, data=payload, headers=self.header)

    def get_running(self, vnf_ip):
        """Return Click status."""

        url = create_url(vnf_ip, 'running')
        payload = {'op': 'GET'}
        return requests.get(url, data=payload, headers=self.header)

    def read_function(self, vnf_ip):
        """Return VNF function content."""

        url = create_url(vnf_ip, 'read_file')
        payload = {'op': 'GET'}
        return requests.get(url, data=payload, headers=self.header)

    def get_vnf_id(self, vnf_ip):
        """Return VNF identification."""

        url = create_url(vnf_ip, 'vnf_identification')
        payload = {'op': 'GET'}
        return requests.get(url, data=payload, headers=self.header)

    def get_log(self, vnf_ip):
        """Return Click log."""

        url = create_url(vnf_ip, 'log')
        payload = {'op': 'GET'}
        return requests.get(url, data=payload, headers=self.header)

    def get_metrics(self, vnf_ip):
        """Return usage metrics from Click."""

        url = create_url(vnf_ip, 'metrics')
        payload = {'op': 'GET'}
        return requests.get(url, data=payload, headers=self.header)

    def write_function(self, vnf_ip, function):
        """Write VNF function."""

        url = create_url(vnf_ip, 'write_file')
        payload = {'path': 'func.click', 'content': function}
        return requests.post(url, data=payload)

    def stop_function(self, vnf_ip):
        """Stop VNF function."""

        url = create_url(vnf_ip, 'stop')
        payload = {'op': 'POST'}
        return requests.post(url, data=payload, headers=self.header)

    def start_function(self, vnf_ip):
        """Start VNF function."""

        url = create_url(vnf_ip, 'start')
        payload = {'op': 'POST'}
        return requests.post(url, data=payload, headers=self.header)
