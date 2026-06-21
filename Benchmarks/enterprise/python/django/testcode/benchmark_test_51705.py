# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest51705(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '{}'.format(auth_header)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
