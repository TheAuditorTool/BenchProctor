# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest62706(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value:.200s}'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
