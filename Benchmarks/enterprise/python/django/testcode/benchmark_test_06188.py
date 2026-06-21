# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest06188(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = to_text(auth_header)
    os.remove(str(data))
    return JsonResponse({"saved": True})
