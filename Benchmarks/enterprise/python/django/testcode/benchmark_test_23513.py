# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23513(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '%s' % str(header_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
