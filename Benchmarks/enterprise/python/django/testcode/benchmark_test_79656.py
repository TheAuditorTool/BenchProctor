# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest79656(request):
    xml_value = request.body.decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})
