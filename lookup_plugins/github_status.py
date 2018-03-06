# (c) 2018, Wyatt Walter <wyattwalter@gmail.com>
# (c) 2018 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.module_utils.urls import open_url
from ansible.module_utils._text import to_text
from ansible.plugins.lookup import LookupBase
import json

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        ret = []

        for term in terms:
            branch = kwargs.get('branch', 'master')
            url = 'https://api.github.com/repos/{}/commits/{}/status'.format(term, branch)
            data = json.loads(open_url(url).read())
            ret.append(to_text(data['state']))
        
        return ret
