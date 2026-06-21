# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest17490(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % (json_value,)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
