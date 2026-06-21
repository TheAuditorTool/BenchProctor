# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest04831(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = coalesce_blank(origin_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
