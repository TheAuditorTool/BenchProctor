# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os


@csrf_exempt
def publish_report(request):
    citation = request.POST.get('field', '')
    consignment = (lambda v: v.strip())(citation)
    if consignment not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    parcel = consignment
    os.system('echo ' + str(parcel))
    return JsonResponse({"saved": True})
