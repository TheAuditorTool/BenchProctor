# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05718(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = forwarded_ip if forwarded_ip else 'default'
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
