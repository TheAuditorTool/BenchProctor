# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
from types import SimpleNamespace


def BenchmarkTest00551(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)
