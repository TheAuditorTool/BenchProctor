# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08661(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
