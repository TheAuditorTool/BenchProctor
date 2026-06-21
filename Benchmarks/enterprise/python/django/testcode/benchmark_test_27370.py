# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest27370(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    os.chmod('/var/app/data/' + str(forwarded_ip), 0o777)
    return JsonResponse({"saved": True})
