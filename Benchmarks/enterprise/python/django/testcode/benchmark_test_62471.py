# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import base64


def BenchmarkTest62471(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
