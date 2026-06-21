# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest42270(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    eval(str(data))
    return JsonResponse({"saved": True})
