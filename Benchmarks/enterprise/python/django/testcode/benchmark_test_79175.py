# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest79175(request):
    user_id = request.GET.get('id', '')
    data = '%s' % (user_id,)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
