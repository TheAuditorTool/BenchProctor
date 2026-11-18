# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00090(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = (lambda v: v.strip())(json_value)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
