# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest00598(request):
    field_value = request.POST.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
