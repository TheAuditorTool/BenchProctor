# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00090(request):
    field_value = request.POST.get('field', '')
    data = '{}'.format(field_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
