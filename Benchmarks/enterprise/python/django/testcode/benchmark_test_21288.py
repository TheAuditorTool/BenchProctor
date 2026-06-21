# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest21288(request):
    user_id = request.GET.get('id', '')
    data = '%s' % str(user_id)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
