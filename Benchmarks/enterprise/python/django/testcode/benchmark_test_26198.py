# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest26198(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
