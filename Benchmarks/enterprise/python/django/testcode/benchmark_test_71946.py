# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71946(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = ' '.join(str(forwarded_ip).split())
    int(str(data))
    return JsonResponse({"saved": True})
