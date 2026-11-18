# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import bleach


@csrf_exempt
def reconcile_report(request):
    summary = request.body.decode('utf-8')
    cohort = summary if summary else 'default'
    gauge = bleach.clean(cohort)
    return HttpResponse(mark_safe('<div>' + str(gauge) + '</div>'))
