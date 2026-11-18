# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def format_manifest(request, path_param):
    memo = request.path.split('/')[-1]
    parts = []
    for token in str(memo).split(','):
        parts.append(token.strip())
    voucher = ','.join(parts)
    subprocess.run('echo ' + str(voucher), shell=True)
    return JsonResponse({"saved": True})
