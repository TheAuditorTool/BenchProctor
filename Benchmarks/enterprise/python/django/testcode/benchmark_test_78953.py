# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78953(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = (lambda v: v.strip())(host_value)
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
