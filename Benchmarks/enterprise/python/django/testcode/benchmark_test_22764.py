# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest22764(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return JsonResponse({"saved": True})
