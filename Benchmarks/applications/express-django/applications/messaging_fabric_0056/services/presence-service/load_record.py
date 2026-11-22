# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def load_record(request):
    footnote = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(footnote)
    if bulletin not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    snippet = bulletin
    os.system('echo ' + str(snippet))
    return JsonResponse({"saved": True})
