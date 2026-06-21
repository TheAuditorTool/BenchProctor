// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05588 {

    @GetMapping("/BenchmarkTest05588")
    public void BenchmarkTest05588(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        if (!headerValue.isEmpty()) throw new Exception("processing error: " + headerValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
