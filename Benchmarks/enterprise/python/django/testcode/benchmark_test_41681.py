# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest41681(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
