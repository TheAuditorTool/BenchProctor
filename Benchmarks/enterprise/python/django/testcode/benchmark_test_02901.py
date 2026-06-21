# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02901(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ua_value if ua_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
