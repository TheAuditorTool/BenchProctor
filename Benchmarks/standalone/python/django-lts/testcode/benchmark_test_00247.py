# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00247(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = f'{header_value!s}'
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})
