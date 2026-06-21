# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37532(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
