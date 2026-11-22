# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def reconcile_header(request):
    note = request.POST.get('field', '')
    cohort = (lambda v: v.strip())(note)
    if cohort not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    gauge = cohort
    os.system('echo ' + str(gauge))
    return JsonResponse({"saved": True})
