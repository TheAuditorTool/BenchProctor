# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest02027(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = '{}'.format(header_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
