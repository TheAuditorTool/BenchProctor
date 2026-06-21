# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest56509(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % (xml_value,)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
