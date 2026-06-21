# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest63789(request):
    xml_value = request.body.decode('utf-8')
    data = '{}'.format(xml_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
