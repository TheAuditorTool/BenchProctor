# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest69280(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    request.session.set_expiry(1800)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
