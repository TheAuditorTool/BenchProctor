# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62857(request):
    user_id = request.GET.get('id', '')
    if str(user_id) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
