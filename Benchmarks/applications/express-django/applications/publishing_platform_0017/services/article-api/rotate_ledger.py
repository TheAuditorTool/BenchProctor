# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def rotate_ledger(request):
    summary = os.environ.get('PUBLISHING_INPUT_0017', '')
    addendum = summary if summary else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(addendum)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    byline = addendum
    subprocess.run('echo ' + str(byline), shell=True)
    return JsonResponse({"saved": True})
