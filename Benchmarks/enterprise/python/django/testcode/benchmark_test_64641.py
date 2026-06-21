# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest64641(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
