import json

import requests
import urllib3

urllib3.disable_warnings()


def login(hostname, username, password):
    url = (f"https://{hostname}/api/fmc_platform/v1/auth/generatetoken")
    token = requests.post(url, data={}, auth=(f'{username}', f'{password}'), verify=False)
    return token.headers["X-auth-access-token"]


def domain_uuid(hostname, token):
    header_domain = {'X-auth-access-token': f'{token}'}
    response_domain = requests.get(f"https://{hostname}/api/fmc_platform/v1/info/domain", headers=header_domain,verify=False)
    uuid = ""
    response = json.loads(response_domain.content)
    for items in response["items"]:
        if items["name"] == "Global":
            uuid = items["uuid"]
    return uuid


def acp_id_by_name(hostname, token, acp_name):
    uuid = domain_uuid(hostname, token)
    header_acp = {'X-auth-access-token': f'{token}'}
    response_acp = requests.get(f"https://{hostname}/api/fmc_config/v1/domain/{uuid}/policy/accesspolicies", headers=header_acp,verify=False)
    response = json.loads(response_acp.content)
    acp_id = ""
    for items in response["items"]:
        if items["name"] == acp_name:
            acp_id = items["id"]
    return acp_id


def acp_rules(hostname, token, acp_name):
    uuid = domain_uuid(hostname, token)
    acp_id = acp_id_by_name(hostname, token, acp_name)
    header_acp = {'X-auth-access-token': f'{token}'}
    response = requests.get(f"https://{hostname}/api/fmc_config/v1/domain/{uuid}/policy/accesspolicies/{acp_id}/accessrules?expanded=true",headers=header_acp, verify=False).json()
    return response["items"]








