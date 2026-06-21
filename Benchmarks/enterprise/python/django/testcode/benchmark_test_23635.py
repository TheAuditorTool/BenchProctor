# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest23635(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    processed = shlex.quote(forwarded_ip)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
