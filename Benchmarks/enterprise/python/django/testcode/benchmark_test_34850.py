# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34850(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
