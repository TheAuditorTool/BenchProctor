# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48078(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
