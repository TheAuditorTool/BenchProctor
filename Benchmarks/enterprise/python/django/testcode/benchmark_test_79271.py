# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os
from types import SimpleNamespace


def BenchmarkTest79271(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    digest = hashlib.pbkdf2_hmac('sha256', str(data).encode(), os.urandom(16), 100000).hex()
    return JsonResponse({'digest': str(digest)}, status=200)
