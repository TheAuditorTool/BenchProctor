# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04784(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    eval(str(data))
    return JsonResponse({"saved": True})
