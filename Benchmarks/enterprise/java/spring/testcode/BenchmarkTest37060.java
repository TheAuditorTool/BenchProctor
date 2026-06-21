// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37060 {

    @GetMapping("/BenchmarkTest37060")
    public void BenchmarkTest37060(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        System.loadLibrary(headerValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
