# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def compact_window(request):
    remark = os.environ.get('WORKSPACE_INPUT_0036', '')
    synopsis = remark if remark else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(synopsis)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    quotation = synopsis
    subprocess.run('echo ' + str(quotation), shell=True)
    return JsonResponse({"saved": True})
