# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest05382(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = normalise_input(multipart_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
