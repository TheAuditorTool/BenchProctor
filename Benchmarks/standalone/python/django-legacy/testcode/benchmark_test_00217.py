# SPDX-License-Identifier: Apache-2.0
import requests
from django.http import HttpResponse


def BenchmarkTest00217(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    kind = 'json' if str(api_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(api_value).strip()
        case _:
            data = str(api_value)
    resp = HttpResponse(status=302)
    resp['Location'] = str(data)
    return resp
