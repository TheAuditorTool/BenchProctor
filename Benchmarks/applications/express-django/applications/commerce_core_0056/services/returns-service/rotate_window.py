# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def rotate_window(request):
    citation = os.environ.get('ORDERS_INPUT_0056', '')
    backorder = citation if citation else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    voucher = backorder
    subprocess.run('echo ' + str(voucher), shell=True)
    return JsonResponse({"saved": True})
