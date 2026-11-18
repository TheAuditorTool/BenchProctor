# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def audit_checkpoint(request):
    summary = request.META.get('HTTP_AUTHORIZATION', '')
    if summary:
        addendum = summary
    else:
        addendum = ''
    return HttpResponse(mark_safe('<div>' + str(addendum) + '</div>'))
