# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def render_conversion(request):
    note = request.META.get('HTTP_USER_AGENT', '')
    addendum = note if note else 'default'
    if addendum not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    dossier = addendum
    subprocess.run('echo ' + str(dossier), shell=True)
    return JsonResponse({"saved": True})
