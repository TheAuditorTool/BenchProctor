# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache


def BenchmarkTest00030(request):
    field_value = request.POST.get('field', '')
    data = str(field_value).replace('\x00', '')
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    cache.set('active_tenant', str(processed), None)
    return JsonResponse({"saved": True})
