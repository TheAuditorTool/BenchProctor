# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69342(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
