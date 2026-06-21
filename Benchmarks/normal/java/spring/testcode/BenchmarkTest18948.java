// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18948 {

    @GetMapping("/BenchmarkTest18948")
    public void BenchmarkTest18948(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        new java.io.File(headerValue).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
