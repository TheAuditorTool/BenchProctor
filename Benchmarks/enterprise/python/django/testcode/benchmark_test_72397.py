# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from types import SimpleNamespace


def BenchmarkTest72397(request):
    cookie_value = request.COOKIES.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    checked_path = os.path.normpath(data)
    with open('/var/uploads/' + str(checked_path), 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
