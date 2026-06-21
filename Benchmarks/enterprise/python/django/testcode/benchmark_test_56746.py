# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest56746(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    base_name = os.path.basename(str(forwarded_ip))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
