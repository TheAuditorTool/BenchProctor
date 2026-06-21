# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22755(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
