# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def fetch_batch(request):
    tagline = os.environ.get('MEDIA_INPUT_0052', '')
    rendition = tagline if tagline else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(rendition)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    montage = rendition
    subprocess.run('echo ' + str(montage), shell=True)
    return JsonResponse({"saved": True})
