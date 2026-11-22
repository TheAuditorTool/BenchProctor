# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache


def BenchmarkTest00163(request):
    upload_name = request.FILES['upload'].name
    parts = str(upload_name).split(',')
    data = ' '.join(parts)
    cache.set('active_tenant', str(data), None)
    return JsonResponse({"saved": True})
