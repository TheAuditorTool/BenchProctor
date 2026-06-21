# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00687(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    base_name = os.path.basename(str(referer_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
