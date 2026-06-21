// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest69821 {

    @GetMapping("/BenchmarkTest69821")
    public void BenchmarkTest69821(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String processed = org.owasp.encoder.Encode.forHtml(originValue);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
