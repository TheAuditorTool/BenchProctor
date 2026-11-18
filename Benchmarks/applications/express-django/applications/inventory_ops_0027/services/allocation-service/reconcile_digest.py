# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def reconcile_digest(request):
    summary = os.environ.get('INVENTORY_INPUT_0027', '')
    restock = summary if summary else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(restock)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    backorder = restock
    subprocess.run('echo ' + str(backorder), shell=True)
    return JsonResponse({"saved": True})
