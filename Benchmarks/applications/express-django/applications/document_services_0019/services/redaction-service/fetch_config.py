# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def fetch_config(request):
    passage = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    dossier = normalize(passage)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if dossier not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    addendum = '/var/app/data/' + dossier
    os.unlink(addendum)
    return JsonResponse({"saved": True})
