# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import pickle


def BenchmarkTest00011(request):
    cookie_value = request.COOKIES.get('session_token', '')
    kind = 'json' if str(cookie_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(cookie_value).strip()
        case _:
            data = str(cookie_value)
    pickle.loads(base64.b64decode(data))
    return JsonResponse({"saved": True})
