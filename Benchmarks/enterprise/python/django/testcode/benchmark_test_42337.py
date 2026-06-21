# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42337(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
