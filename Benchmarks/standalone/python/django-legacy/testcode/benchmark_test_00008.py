# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.core.cache import cache
import re


def BenchmarkTest00008(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    cache.set('active_tenant', str(processed), None)
    return JsonResponse({"saved": True})
