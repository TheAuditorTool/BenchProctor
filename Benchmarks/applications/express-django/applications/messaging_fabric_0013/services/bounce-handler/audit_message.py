# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def audit_message(request):
    summary = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(summary)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if bulletin not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    snippet = '/var/app/data/' + bulletin
    os.unlink(snippet)
    return JsonResponse({"saved": True})
