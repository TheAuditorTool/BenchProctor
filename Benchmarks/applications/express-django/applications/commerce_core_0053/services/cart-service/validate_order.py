# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def validate_order(request):
    memo = os.environ.get('ORDERS_INPUT_0053', '')
    voucher = memo if memo else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(voucher)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    backorder = voucher
    subprocess.run('echo ' + str(backorder), shell=True)
    return JsonResponse({"saved": True})
