# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import subprocess


@csrf_exempt
def annotate_threshold(request):
    heading = request.META.get('HTTP_USER_AGENT', '')
    consignment = heading if heading else 'default'
    if consignment not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    parcel = consignment
    subprocess.run('echo ' + str(parcel), shell=True)
    return JsonResponse({"saved": True})
