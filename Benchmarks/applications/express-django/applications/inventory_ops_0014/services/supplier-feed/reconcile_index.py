# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def reconcile_index(request):
    excerpt = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    restock = normalize(excerpt)
    if restock not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    backorder = restock
    os.system('echo ' + str(backorder))
    return JsonResponse({"saved": True})
