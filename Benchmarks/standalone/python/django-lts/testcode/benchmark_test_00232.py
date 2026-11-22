# SPDX-License-Identifier: Apache-2.0
import json
from django.http import HttpResponse
from django.template import Template, Context


def BenchmarkTest00232(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = json.loads(json_value).get('value', '')
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(data)}))
    return HttpResponse(page)
