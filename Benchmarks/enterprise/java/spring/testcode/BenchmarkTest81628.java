// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest81628 {

    @GetMapping("/BenchmarkTest81628")
    public void BenchmarkTest81628(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        if (!headerValue.isEmpty()) throw new Exception("processing error: " + headerValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
