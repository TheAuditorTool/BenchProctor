# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context
import json


def BenchmarkTest00193(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    page = Template('<div>{{ value }}</div>').render(Context({'value': str(data)}))
    return HttpResponse(page)
