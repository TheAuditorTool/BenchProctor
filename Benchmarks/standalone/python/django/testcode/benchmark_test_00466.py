# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00466(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(auth_header))
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
