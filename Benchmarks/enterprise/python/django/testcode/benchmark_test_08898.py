# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest08898(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
