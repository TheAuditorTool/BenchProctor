# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def collect_receipt(request):
    snippet = request.META.get('HTTP_USER_AGENT', '')
    persona = snippet if snippet else 'default'
    if persona not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    synopsis = persona
    subprocess.run('echo ' + str(synopsis), shell=True)
    return JsonResponse({"saved": True})
