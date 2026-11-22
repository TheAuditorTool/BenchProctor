# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def compact_config(request):
    citation = request.POST.get('field', '')
    parcel = (lambda v: v.strip())(citation)
    if parcel not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    consignment = parcel
    os.system('echo ' + str(consignment))
    return JsonResponse({"saved": True})
