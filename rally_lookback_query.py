import json
import pprint

from rally_lookback_connection_helper import rally_lookback_connection_helper

lbapi_config = {
    "base_url"      : "https://rally1.rallydev.com",
    "lbapi_version" : "v2.0",
    "apikey"        : "_vwU0V4x9s0Opa7a29gThDRkHhs4dZ5r9",
    "workspace_oid" : "12345678910"
}

# lbapi_config = {
#     "base_url"      :  "https://rally1.rallydev.com",
#     "lbapi_version" :  "v2.0",
#     "username"      :  "user@company.com",
#     "password"      :  "t0p$3cr3t",
#     "workspace_oid" :  "12345678910"
# }

my_lbapi = rally_lookback_connection_helper(lbapi_config)

query_dict = {
    "find": {
        "FormattedID": "DE9",
        "__At": "current"
    },
    "fields": True,
    "start": 0,
    "pagesize": 10,
    "removeUnauthorizedSnapshots": True
}

lbapi_results = my_lbapi.query(query_dict)
print json.dumps(lbapi_results, sort_keys=False, indent=4, separators=(',', ': '))