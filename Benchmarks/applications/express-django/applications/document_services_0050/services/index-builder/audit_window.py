# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def audit_window(request):
    citation = request.GET.get('id', '')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    dossier = ','.join(parts)
    subprocess.run(['echo', dossier], shell=False)
    return JsonResponse({"saved": True})
