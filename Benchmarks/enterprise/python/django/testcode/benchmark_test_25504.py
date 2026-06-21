# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import json


def BenchmarkTest25504(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
