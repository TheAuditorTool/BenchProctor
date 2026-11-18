# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess
import os
import re


@csrf_exempt
def export_window(request):
    excerpt = os.environ.get('PLATFORM_INPUT_0021', '')
    handshake = excerpt if excerpt else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(handshake)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    persona = handshake
    subprocess.run('echo ' + str(persona), shell=True)
    return JsonResponse({"saved": True})
