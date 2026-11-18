# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def collect_label(request, path_param):
    caption = request.path.split('/')[-1]
    parts = []
    for token in str(caption).split(','):
        parts.append(token.strip())
    parcel = ','.join(parts)
    subprocess.run('echo ' + str(parcel), shell=True)
    return JsonResponse({"saved": True})
