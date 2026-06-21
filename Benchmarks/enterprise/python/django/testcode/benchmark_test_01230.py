# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def normalise_input(value):
    return value.strip()

def BenchmarkTest01230(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = normalise_input(forwarded_ip)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
