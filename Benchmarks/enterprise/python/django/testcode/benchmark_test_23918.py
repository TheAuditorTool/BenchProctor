# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23918(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    eval(str(data))
    return JsonResponse({"saved": True})
