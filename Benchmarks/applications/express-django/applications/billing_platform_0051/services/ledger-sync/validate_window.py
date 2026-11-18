# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def validate_window(request):
    synopsis = os.environ.get('BILLING_INPUT_0051', '')
    arrears = synopsis if synopsis else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(arrears)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    dunning = arrears
    subprocess.run('echo ' + str(dunning), shell=True)
    return JsonResponse({"saved": True})
