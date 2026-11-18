# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def reconcile_batch(request):
    summary = os.environ.get('RISK_INPUT_0030', '')
    grievance = summary if summary else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(grievance)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    verdict = grievance
    subprocess.run('echo ' + str(verdict), shell=True)
    return JsonResponse({"saved": True})
