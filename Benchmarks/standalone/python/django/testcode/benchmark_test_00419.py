# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest00419(request):
    field_value = request.POST.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
