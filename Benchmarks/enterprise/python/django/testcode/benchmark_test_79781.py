# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79781(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
