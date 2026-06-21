# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest37902(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
