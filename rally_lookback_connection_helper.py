import sys, os
import requests
import json


class rally_lookback_connection_helper(object):

    def __init__(self, config):
        self.base_url          = config.get('base_url', 'https://rally1.rallydev.com') # LBAPI base url
        self.lbapi_version     = config.get('lbapi_version', 'v2.0')  # LBAPI version, i.e. 'v2.0'
        self.workspace_oid     = config['workspace_oid']              # OID of the Rally Workspace
        self.config            = config

        # Instantiate a session with some default configuration params
        self.session           = requests.Session()
        self.session.timeout   = 10.0
        self.session.verify    = True

        # setup the client authentication method
        self.set_client_auth()

        # setup query_url
        self.query_url         = self.make_query_url()

    # Client authentication settings
    def set_client_auth(self):
        self.session.headers                   = {}
        if self.config.get('apikey', None):
            self.apikey                        = self.config['apikey']
            self.session.headers['ZSESSIONID'] = self.apikey
            self.user                          = None
            self.password                      = None
        else:
            self.username     = self.config['username']
            self.password     = self.config['password']
            self.session.auth = requests.auth.HTTPBasicAuth(self.username, self.password)

    # Lookback query url
    def make_query_url(self):
        return "%s/analytics/%s/service/rally/workspace/%s/artifact/snapshot/query" % (self.base_url, self.lbapi_version, self.workspace_oid)

    # query method
    def query(self, query_dict):
        response_dict = {}
        payload = json.dumps(query_dict)
        response = self.session.post(self.query_url, data=payload, headers=self.session.headers)
        if response.status_code != 200:
            warning("Error querying Lookback API")
        else:
            response_dict = json.loads(response.text, 'utf-8')
        return response_dict