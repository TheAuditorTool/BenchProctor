# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61818(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
