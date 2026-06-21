// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66576 {

    @GetMapping("/BenchmarkTest66576")
    public void BenchmarkTest66576(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String processed = org.owasp.encoder.Encode.forHtml(uaValue);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
