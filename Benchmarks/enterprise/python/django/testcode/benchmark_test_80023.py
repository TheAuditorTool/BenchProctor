# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest80023(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    int(str(data))
    return JsonResponse({"saved": True})
