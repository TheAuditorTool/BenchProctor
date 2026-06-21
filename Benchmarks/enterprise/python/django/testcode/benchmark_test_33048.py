# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33048(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    eval(str(auth_header))
    return JsonResponse({"saved": True})
