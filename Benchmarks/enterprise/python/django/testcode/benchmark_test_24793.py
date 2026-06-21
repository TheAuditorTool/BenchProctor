# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24793(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if str(forwarded_ip).endswith(('.prod.internal', '.trusted.net')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
