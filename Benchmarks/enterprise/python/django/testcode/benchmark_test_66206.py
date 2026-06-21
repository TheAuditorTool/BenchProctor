# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
from types import SimpleNamespace


def BenchmarkTest66206(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(target_url)})
