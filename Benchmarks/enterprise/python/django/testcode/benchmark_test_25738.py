# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
from urllib.parse import unquote


def BenchmarkTest25738(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
