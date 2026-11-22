# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import defusedxml.ElementTree


def BenchmarkTest00128(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
