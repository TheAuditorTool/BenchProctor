# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest72479(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = default_blank(multipart_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
