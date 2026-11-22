# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache


def BenchmarkTest00180(request):
    field_value = request.POST.get('field', '')
    parts = str(field_value).split(',')
    data = ' '.join(parts)
    cache.set('active_tenant', str(data), None)
    return JsonResponse({"saved": True})
