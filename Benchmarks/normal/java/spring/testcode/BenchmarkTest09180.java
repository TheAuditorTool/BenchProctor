// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09180 {

    @GetMapping("/BenchmarkTest09180")
    public void BenchmarkTest09180(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(headerValue);
        String data = carrier.toString();
        response.sendError(500, data);
    }
}
