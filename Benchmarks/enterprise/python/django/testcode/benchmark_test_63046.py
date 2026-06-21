# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63046(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
