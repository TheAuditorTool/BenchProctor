# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest79034(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    os.remove(str(data))
    return JsonResponse({"saved": True})
