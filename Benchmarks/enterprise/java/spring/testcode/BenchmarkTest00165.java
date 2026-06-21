// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00165 {

    @GetMapping("/BenchmarkTest00165")
    public void BenchmarkTest00165(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        Integer.parseInt(headerValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
