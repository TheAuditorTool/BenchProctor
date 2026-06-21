# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest12847(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
