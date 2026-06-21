# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest06384(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
