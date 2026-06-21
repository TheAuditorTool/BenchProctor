# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest71012(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = to_text(header_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
