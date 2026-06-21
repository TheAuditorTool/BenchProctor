# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import html
from types import SimpleNamespace


def BenchmarkTest29208(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    processed = str(data).replace("<script", "")
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
