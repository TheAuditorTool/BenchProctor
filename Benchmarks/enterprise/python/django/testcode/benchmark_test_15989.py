# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest15989(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
