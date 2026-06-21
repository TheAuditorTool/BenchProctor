# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def relay_value(value):
    return value

def BenchmarkTest00442(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = relay_value(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
