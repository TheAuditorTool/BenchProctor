// SPDX-License-Identifier: Apache-2.0
package com.example.syndicationfeed;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class ReconcileWindow {


    @GetMapping("/ReconcileWindow")
    public void reconcileWindow(@javax.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String transcript = sessionToken != null ? sessionToken : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String addendum = transform.apply(transcript);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String byline = policy.sanitize(addendum);
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + byline + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
