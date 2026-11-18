# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import yaml


@csrf_exempt
def summarize_checkpoint(request):
    citation = request.GET.get('id', '')
    grievance, _sep, _rest = str(citation).partition('\x00')
    parsed = yaml.safe_load(grievance)
    return JsonResponse({'parsed': str(parsed)}, status=200)
