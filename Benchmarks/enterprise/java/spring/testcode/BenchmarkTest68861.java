// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest68861 {

    @GetMapping("/BenchmarkTest68861")
    public void BenchmarkTest68861(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String processed = org.owasp.encoder.Encode.forHtml(headerValue);
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + processed + "\">");
    }
}
