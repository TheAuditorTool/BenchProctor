// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80376 {

    @GetMapping("/BenchmarkTest80376")
    public void BenchmarkTest80376(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(hostValue)); }
        catch (NumberFormatException e) { data = hostValue; }
        org.owasp.html.PolicyFactory policy = new org.owasp.html.HtmlPolicyBuilder().allowCommonInlineFormattingElements().toFactory();
        String processed = policy.sanitize(data);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
