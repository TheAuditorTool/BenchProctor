# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45352(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip}'
    int(str(data))
    return JsonResponse({"saved": True})
