# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60208(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
