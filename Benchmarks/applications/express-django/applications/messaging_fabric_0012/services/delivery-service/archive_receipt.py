# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def archive_receipt(request):
    preface = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(preface)
    if bulletin not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    citation = bulletin
    os.system('echo ' + str(citation))
    return JsonResponse({"saved": True})
