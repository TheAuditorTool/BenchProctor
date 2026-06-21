# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import auth_check


def BenchmarkTest22584(request):
    raw_body = request.body.decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    auth_check('user', data)
    return JsonResponse({"saved": True})
