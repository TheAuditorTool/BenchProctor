# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74722(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
