# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def export_record(request, path_param):
    excerpt = request.path.split('/')[-1]
    handshake = (lambda v: v.strip())(excerpt)
    subprocess.Popen('echo ' + str(handshake), shell=True).wait()
    return JsonResponse({"saved": True})
