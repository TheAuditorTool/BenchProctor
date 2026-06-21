# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest25263(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
