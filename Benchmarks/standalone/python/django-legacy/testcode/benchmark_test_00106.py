# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest00106(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
