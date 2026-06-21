# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38487(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
