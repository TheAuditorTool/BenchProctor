# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63566(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
