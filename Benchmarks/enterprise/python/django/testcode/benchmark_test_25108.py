# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest25108(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    os.remove(str(data))
    return JsonResponse({"saved": True})
