# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest18263(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
