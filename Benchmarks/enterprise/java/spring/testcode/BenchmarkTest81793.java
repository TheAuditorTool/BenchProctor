// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81793 {

    @GetMapping("/BenchmarkTest81793")
    public void BenchmarkTest81793(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data;
        if (cookieValue.length() > 256) { data = cookieValue.substring(0, 256); }
        else { data = cookieValue; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String processed = policy.sanitize(data);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
