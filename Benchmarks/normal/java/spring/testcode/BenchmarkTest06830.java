// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06830 {

    @GetMapping("/BenchmarkTest06830")
    public void BenchmarkTest06830(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String processed = org.owasp.encoder.Encode.forHtml(forwardedIp);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
