# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from types import SimpleNamespace


def BenchmarkTest30635(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
