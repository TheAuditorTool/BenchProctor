# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30818(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
