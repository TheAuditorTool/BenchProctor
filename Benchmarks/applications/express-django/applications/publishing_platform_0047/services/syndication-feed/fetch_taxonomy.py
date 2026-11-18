# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def fetch_taxonomy(request):
    synopsis = os.environ.get('PUBLISHING_INPUT_0047', '')
    byline = synopsis if synopsis else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(byline)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    addendum = byline
    subprocess.run('echo ' + str(addendum), shell=True)
    return JsonResponse({"saved": True})
