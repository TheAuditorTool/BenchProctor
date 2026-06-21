# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def normalise_input(value):
    return value.strip()

def BenchmarkTest23346(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = normalise_input(forwarded_ip)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
