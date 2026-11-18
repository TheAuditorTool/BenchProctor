# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def normalize_receipt(request):
    footnote = os.environ.get('MESSAGING_INPUT_0034', '')
    bulletin = footnote if footnote else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(bulletin)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    heading = bulletin
    subprocess.run('echo ' + str(heading), shell=True)
    return JsonResponse({"saved": True})
