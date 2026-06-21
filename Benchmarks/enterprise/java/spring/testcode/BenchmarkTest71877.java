// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71877 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest71877")
    public void BenchmarkTest71877(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = normalize(headerValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
