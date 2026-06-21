# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest76473(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    os.remove(str(data))
    return JsonResponse({"saved": True})
