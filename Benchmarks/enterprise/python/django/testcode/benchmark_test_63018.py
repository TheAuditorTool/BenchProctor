# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63018(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % (header_value,)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})
