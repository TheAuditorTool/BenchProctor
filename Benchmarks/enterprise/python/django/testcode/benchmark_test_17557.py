# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest17557(request):
    cookie_value = request.COOKIES.get('session_token', '')
    subprocess.run([str(cookie_value), '--status'], shell=False)
    return JsonResponse({"saved": True})
