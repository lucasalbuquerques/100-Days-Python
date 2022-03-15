import teste01
import pandas as pd
import json

hostname = "fmcrestapisandbox.cisco.com"
username = "lucas.albu"
password = "eNFEvaGt"
acp_name = "mb-test-01"

token = teste01.login(hostname, username, password)
teste = teste01.acp_rules(hostname, token, acp_name)


for items in teste:
    # Forma de acessar as informações quando não sao uma lista
    if items.get("sourceNetworks"):
        name_source_network = items['sourceNetworks']['objects'][0]
        print(name_source_network['name'])







