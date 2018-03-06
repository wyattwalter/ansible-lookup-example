# (c) 2018, Wyatt Walter <wyattwalter@gmail.com>
# (c) 2018 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from ansible.module_utils._text import to_text
from ansible.plugins.lookup import LookupBase
import json
import urllib2

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        req = urllib2.Request('https://api.chucknorris.io/jokes/random', headers={ 'User-Agent': 'Mozilla/5.0' })
        data = json.loads(urllib2.urlopen(req).read())
        return [to_text(data['value'])]
