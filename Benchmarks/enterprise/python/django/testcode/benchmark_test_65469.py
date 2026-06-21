# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest65469(request):
    cookie_value = request.COOKIES.get('session_token', '')
    os.chmod('/var/app/data/' + str(cookie_value), 0o777)
    return JsonResponse({"saved": True})
