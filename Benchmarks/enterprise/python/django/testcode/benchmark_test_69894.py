# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69894(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return JsonResponse({"saved": True})
