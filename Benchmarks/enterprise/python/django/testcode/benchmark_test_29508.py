# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import tempfile


def BenchmarkTest29508(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
