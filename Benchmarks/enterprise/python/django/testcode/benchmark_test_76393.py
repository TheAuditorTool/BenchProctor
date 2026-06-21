# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from urllib.parse import unquote
from django.http import HttpResponse


def BenchmarkTest76393(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
