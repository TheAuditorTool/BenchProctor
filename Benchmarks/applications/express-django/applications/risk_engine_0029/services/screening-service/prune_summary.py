# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def prune_summary(request):
    subject = request.body.decode('utf-8')
    grievance = subject if subject else 'default'
    parsed = yaml.safe_load(grievance)
    return JsonResponse({'parsed': str(parsed)}, status=200)
