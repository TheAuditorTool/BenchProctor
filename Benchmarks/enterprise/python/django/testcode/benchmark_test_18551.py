# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18551(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    if str(data) == 'is_admin':
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})
