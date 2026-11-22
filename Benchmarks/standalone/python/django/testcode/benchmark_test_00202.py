# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00202(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
