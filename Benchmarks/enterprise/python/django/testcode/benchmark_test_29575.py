# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest29575(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
