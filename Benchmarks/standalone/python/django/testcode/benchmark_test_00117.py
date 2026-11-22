# SPDX-License-Identifier: Apache-2.0
from django.http import HttpResponse
from django.template import Template, Context
import json


def BenchmarkTest00117(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    page = Template('<div>{{ value|safe }}</div>').render(Context({'value': str(data)}))
    return HttpResponse(page)
