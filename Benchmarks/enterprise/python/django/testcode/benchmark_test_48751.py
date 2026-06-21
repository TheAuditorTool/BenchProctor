# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest48751(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = coalesce_blank(header_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
