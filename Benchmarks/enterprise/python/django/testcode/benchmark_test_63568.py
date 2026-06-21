# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def relay_value(value):
    return value

def BenchmarkTest63568(request):
    user_id = request.GET.get('id', '')
    data = relay_value(user_id)
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
