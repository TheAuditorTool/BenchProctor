# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from pathlib import Path


def BenchmarkTest00043(request):
    json_value = json.loads(request.body or b'{}').get('payload', '')
    data = json_value if json_value else 'default'
    Path('/var/app/data/' + str(data)).write_text('data')
    return JsonResponse({"saved": True})
