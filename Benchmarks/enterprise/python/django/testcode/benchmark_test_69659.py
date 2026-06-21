# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69659(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if len(str(data)) >= 4:
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
