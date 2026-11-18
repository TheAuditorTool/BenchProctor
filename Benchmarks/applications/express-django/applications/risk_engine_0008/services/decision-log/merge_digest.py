# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def merge_digest(request):
    synopsis = request.body.decode('utf-8')
    verdict = synopsis if synopsis else 'default'
    grievance = bleach.clean(verdict)
    return HttpResponse(mark_safe('<div>' + str(grievance) + '</div>'))
