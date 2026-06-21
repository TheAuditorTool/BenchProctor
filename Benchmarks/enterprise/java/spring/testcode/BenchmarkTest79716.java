// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79716 {

    @GetMapping("/BenchmarkTest79716")
    public void BenchmarkTest79716(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.List<String> tokens = java.util.Arrays.asList(headerValue.split(","));
        String data = String.join(",", tokens);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
