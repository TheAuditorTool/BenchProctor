# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def validate_bundle(request):
    phrase = request.body.decode('utf-8')
    inquiry = phrase if phrase else 'default'
    grievance = bleach.clean(inquiry)
    return HttpResponse(mark_safe('<div>' + str(grievance) + '</div>'))
