# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def normalize_record(request):
    heading = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    handshake = normalize(heading)
    if handshake not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    remark = handshake
    os.system('echo ' + str(remark))
    return JsonResponse({"saved": True})
