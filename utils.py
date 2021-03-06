# Tacker REST API status codes
status = {
    200: 'OK.',
    201: 'Created.',
    204: 'No Content.',
    400: 'Bad Request.',
    401: 'Unauthorized.',
    404: 'Not Found.',
    409: 'Conflict.',
    500: 'Internal Server Error.'
}

# common used status
OK      = 'OK'
ERROR   = 'ERROR'
TIMEOUT = 'TIMEOUT'
ACTIVE  = 'ACTIVE'
OPTIONS = 'OPTIONS'

# SFC network source traffic
INTERNAL = '1'
EXTERNAL = '2'

# VNF types
CLICK_VNF = 'click'
GENERAL_VNF = 'general'


# Click on OSv URL
def create_url(vnf_ip, task):
    return ''.join(['http://', vnf_ip, ':8000/click_plugin/', task])


# used as a template to create a new VNFFG
vnffgd_template = {
    "vnffgd": {
        "name": "vnffgd1",
        "template": {
            "vnffgd": {
                "tosca_definitions_version": "tosca_simple_profile_for_nfv_1_0_0",
                "description": "Sample VNFFG template",
                "topology_template": {
                    "node_templates": {
                        "Forwarding_path1": {
                            "type": "tosca.nodes.nfv.FP.Tacker",
                            "description": "creates path (CP12->CP22)",
                            "properties": {
                                "policy": {
                                    "type": "ACL",
                                    "criteria": []
                                },
                                "path": [],
                                "id": 0
                            }
                        }
                    },
                    "description": "Sample VNFFG template",
                    "groups": {
                        "VNFFG1": {
                            "type": "tosca.groups.nfv.VNFFG",
                            "description": "HTTP to Corporate Net",
                            "members": [
                                "Forwarding_path1"
                            ],
                            "properties": {
                                "vendor": "tacker",
                                "connection_point": [],
                                "version": 1.0,
                                "constituent_vnfs": [],
                                "number_of_endpoints": 0,
                                "dependent_virtual_link": []
                            }
                        }
                    }
                }
            }
        }
    }
}
