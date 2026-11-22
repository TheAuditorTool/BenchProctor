# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path


def BenchmarkTest00044(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '{}'.format(host_value)
    Path('/var/app/data/' + str(data)).write_text('data')
    return JsonResponse({"saved": True})
