# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def audit_batch(request):
    subject = os.environ.get('MESSAGING_INPUT_0003', '')
    bulletin = subject if subject else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    passage = bulletin
    subprocess.run('echo ' + str(passage), shell=True)
    return JsonResponse({"saved": True})
