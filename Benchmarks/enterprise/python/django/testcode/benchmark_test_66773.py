# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from urllib.parse import unquote


def BenchmarkTest66773(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
