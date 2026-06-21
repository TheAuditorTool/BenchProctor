// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79936 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest79936")
    public void BenchmarkTest79936(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = normalize(headerValue);
        if (!data.isEmpty()) throw new IllegalArgumentException("invalid input: " + data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
