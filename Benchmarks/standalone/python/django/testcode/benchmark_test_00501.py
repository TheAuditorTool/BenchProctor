# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import defusedxml.ElementTree


def BenchmarkTest00501(request):
    field_value = request.POST.get('field', '')
    data = unquote(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
