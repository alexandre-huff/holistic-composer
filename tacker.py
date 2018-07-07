#!/usr/bin/env python

import configparser
import os
import requests
import logging


logger = logging.getLogger('tacker')


class IdentityManager:
    """
    Class responsible for identification and authentication of REST requests.
    """

    def __init__(self):
        CONFIG_FILE = 'tacker.conf'
        if not os.path.isfile(CONFIG_FILE):
            logger.critical("Missing tacker.conf file!")
            exit(1)

        config = configparser.ConfigParser()
        config.read(CONFIG_FILE)

        self.OPENSTACK_URL = config.get('openstack', 'url')
        self.USERNAME      = config.get('auth', 'username')
        self.TENANT_NAME   = config.get('auth', 'tenant_name')
        self.PASSWORD      = config.get('auth', 'password')
        self.FIP_INTERFACES = config['sfc_fip_router_interface']

        self.header = {
            'Content-type' : 'application/json',
            'Accept'       : 'application/json'
        }

        self.identity_info = self.get_identity_info()

    def get_fip_router_interfaces(self):
        """Return all FIP network configured interfaces in tacker.conf file

        :return: a dictionary containing all FIP network configured interfaces in tacker.conf file
        """

        return self.FIP_INTERFACES

    def get_identity_info(self):
        """
        Request for tokens and endpoints info.
        """

        data = """{
            "auth": {
                "tenantName": "%s",
                "passwordCredentials": {
                    "username": "%s",
                    "password": "%s"
                }
            }
        }""" % (self.TENANT_NAME, self.USERNAME, self.PASSWORD)

        url = self.OPENSTACK_URL + 'identity/v2.0/tokens'
        return requests.post(url, data=data, headers=self.header).json()

    def get_token(self):
        """
        Return the token ID used to authenticate requests.
        """

        return self.identity_info['access']['token']['id']

    def get_endpoints(self):
        """
        Get endpoints public URLs of each OpenStack service.
        These endpoints are used for future requests.
        """

        endpoints = {}
        service_catalog = self.identity_info['access']['serviceCatalog']

        for service in service_catalog:
            name = service['name']
            public_url = service['endpoints'][0]['publicURL']
            endpoints[name] = public_url

        return endpoints


class Tacker:
    """
    Implementation of the Tacker Client REST API interface.
    """

    def __init__(self, token, tacker_endpoint):
        self.token = token
        self.header = {
            'Content-type' : 'application/json',
            'Accept'       : 'application/json',
            'X-Auth-Token' : token
        }
        self.tacker_endpoint = tacker_endpoint

    def vnfd_create(self, vnfd):
        """
        Create a VNF descriptor.
        Template should be a JSON text.
        """

        url = self.tacker_endpoint + 'v1.0/vnfds'
        return requests.post(url, headers=self.header, data=vnfd)

    def vnfd_delete(self, vnfd_id):
        """
        Delete a given VNF descriptor.
        """

        url = self.tacker_endpoint + 'v1.0/vnfds/' + vnfd_id
        return requests.delete(url, headers=self.header)

    def vnfd_list(self):
        """
        List all available VNF descriptors.
        """

        url = self.tacker_endpoint + 'v1.0/vnfds'
        return requests.get(url, headers=self.header)

    def vnf_create(self, vnfd_id, vnf_name):
        """
        Create a instance of a VNF.
        """

        url = self.tacker_endpoint + 'v1.0/vnfs'
        data = """{
            "vnf": {
                "attributes": {},
                "vim_id": "",
                "description": "",
                "vnfd_id": "%s",
                "name": "%s"
            }
        }""" % (vnfd_id, vnf_name)

        return requests.post(url, headers=self.header, data=data)

    def vnffgd_create(self, vnffgd):
        """Create a VNF Forwarding Graph Descriptor."""

        url = self.tacker_endpoint + 'v1.0/vnffgds'
        return requests.post(url, headers=self.header, data=vnffgd)

    def vnffgd_list(self):
        """List all VNFFG Descriptors in Tacker"""

        url = self.tacker_endpoint + 'v1.0/vnffgds'
        return requests.get(url, headers=self.header)

    def vnffgd_delete(self, vnffgd_id):
        """Delete a given VNFFGD"""

        url = self.tacker_endpoint + 'v1.0/vnffgds/' + vnffgd_id
        return requests.delete(url, headers=self.header)

    def vnffg_create(self, vnffgd_id, vnf_mapping, vnffg_name):
        """Create a VNF Forwarding Graph."""

        url = self.tacker_endpoint + 'v1.0/vnffgs'
        vnffg = """{
            "vnffg": {
                "vnffgd_id": "%s",
                "name": "%s",
                "vnf_mapping": %s,
                "symmetrical": false
            }
        }""" % (vnffgd_id, vnffg_name, vnf_mapping)

        logger.info(vnffg)

        return requests.post(url, headers=self.header, data=vnffg)

    def vnffg_list(self):
        """List all VNF Forwarding Graph in Tacker"""

        url = self.tacker_endpoint + 'v1.0/vnffgs'
        return requests.get(url, headers=self.header)

    def vnffg_show(self, vnffg_id):
        """List a given VNF Forwarding Graph in Tacker"""

        url = self.tacker_endpoint + 'v1.0/vnffgs/' + vnffg_id
        return requests.get(url, headers=self.header)

    def vnffg_delete(self, vnffg_id):
        """Delete a given VNF Forwarding Graph in Tacker"""

        url = self.tacker_endpoint + 'v1.0/vnffgs/' + vnffg_id
        return requests.delete(url, headers=self.header)

    def vnf_delete(self, vnf_id):
        """
        Delete a given VNF.
        """

        url = self.tacker_endpoint + 'v1.0/vnfs/' + vnf_id
        return requests.delete(url, headers=self.header)

    def vnf_update(self, vnf_id, update_file):
        """
        Update a given VNF.
        """

        url = self.tacker_endpoint + 'v1.0/vnfs/' + vnf_id
        return requests.put(url, headers=self.header, data=update_file)

    def vnf_list(self):
        """
        List all VNFs.
        """

        url = self.tacker_endpoint + 'v1.0/vnfs'
        return requests.get(url, headers=self.header)

    def vnf_show(self, vnf_id):
        """
        Show info about a given VNF.
        """

        url = self.tacker_endpoint + 'v1.0/vnfs/' + vnf_id
        return requests.get(url, headers=self.header)

    def vnf_resources(self, vnf_id):
        """
        Show VDU and CP of a given VNF.
        """

        url = self.tacker_endpoint + 'v1.0/vnfs/%s/resources' % vnf_id
        return requests.get(url, headers=self.header)

    def sfc_list(self):
        """List all SFCs."""

        url = self.tacker_endpoint + 'v1.0/sfcs'
        return requests.get(url, headers=self.header)
