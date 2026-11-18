# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def load_threshold(request):
    summary = request.META.get('HTTP_AUTHORIZATION', '')
    grievance = (lambda v: v.strip())(summary)
    return HttpResponse(mark_safe('<div>' + str(grievance) + '</div>'))
