# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78850(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
