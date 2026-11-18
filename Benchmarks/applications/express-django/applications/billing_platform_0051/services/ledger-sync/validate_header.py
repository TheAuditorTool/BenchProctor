# SPDX-License-Identifier: Apache-2.0
from django.views.decorators.csrf import csrf_exempt
from django.utils.safestring import mark_safe
from django.http import HttpResponse


@csrf_exempt
def validate_header(request):
    synopsis = request.META.get('HTTP_USER_AGENT', '')
    arrears = '%s' % (synopsis,)
    return HttpResponse(mark_safe('<div>' + str(arrears) + '</div>'))
