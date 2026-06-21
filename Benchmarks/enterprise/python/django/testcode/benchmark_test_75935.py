# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75935(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    int(str(data))
    return JsonResponse({"saved": True})
