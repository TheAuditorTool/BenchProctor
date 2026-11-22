# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def format_asset(request):
    snippet = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    montage = normalize(snippet)
    if montage not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    rendition = montage
    os.system('echo ' + str(rendition))
    return JsonResponse({"saved": True})
