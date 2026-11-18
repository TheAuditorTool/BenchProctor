# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def build_decision(request):
    summary = request.body.decode('utf-8')
    grievance = summary if summary else 'default'
    verdict = bleach.clean(grievance)
    return HttpResponse(mark_safe('<div>' + str(verdict) + '</div>'))
