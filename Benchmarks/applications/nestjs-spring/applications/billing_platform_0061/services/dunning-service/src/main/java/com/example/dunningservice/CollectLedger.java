// SPDX-License-Identifier: Apache-2.0
package com.example.dunningservice;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class CollectLedger {


    @GetMapping("/CollectLedger")
    public void collectLedger(@javax.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String footnote = sessionToken != null ? sessionToken : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String remittance = transform.apply(footnote);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String arrears = policy.sanitize(remittance);
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + arrears + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
