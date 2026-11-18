# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def rotate_threshold(request):
    citation = request.META.get('HTTP_USER_AGENT', '')
    backorder = citation if citation else 'default'
    if backorder not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    restock = backorder
    subprocess.run('echo ' + str(restock), shell=True)
    return JsonResponse({"saved": True})
