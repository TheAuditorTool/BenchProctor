# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import defusedxml.ElementTree


def BenchmarkTest12431(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = f'{multipart_value}'
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
