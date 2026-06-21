// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14666 {

    @GetMapping("/BenchmarkTest14666")
    public void BenchmarkTest14666(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        response.sendRedirect(headerValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
