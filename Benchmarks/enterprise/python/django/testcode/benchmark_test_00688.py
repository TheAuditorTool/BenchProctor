# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00688(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    eval(str(data))
    return JsonResponse({"saved": True})
