# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def validate_schedule(request):
    preface = request.body.decode('utf-8')
    bulletin = preface if preface else 'default'
    notice = bleach.clean(bulletin)
    return HttpResponse(mark_safe('<div>' + str(notice) + '</div>'))
