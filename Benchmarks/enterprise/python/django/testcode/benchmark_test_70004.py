# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest70004(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = to_text(multipart_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
