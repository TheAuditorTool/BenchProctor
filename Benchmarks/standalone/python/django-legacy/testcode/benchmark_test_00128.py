# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest00128(request):
    field_value = request.POST.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
