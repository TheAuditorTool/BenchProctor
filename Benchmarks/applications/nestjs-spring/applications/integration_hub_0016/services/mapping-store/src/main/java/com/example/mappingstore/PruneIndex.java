// SPDX-License-Identifier: Apache-2.0
package com.example.mappingstore;
import org.springframework.web.bind.annotation.*;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@RestController
class PruneIndex {


    @GetMapping("/PruneIndex")
    public void pruneIndex(@javax.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String wording = sessionToken != null ? sessionToken : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String handshake = transform.apply(wording);
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String subject = policy.sanitize(handshake);
        response.setContentType("text/html;charset=UTF-8");
        response.getOutputStream().write(("<div class=\"comment\">" + subject + "</div>").getBytes(java.nio.charset.StandardCharsets.UTF_8));
    }
}
