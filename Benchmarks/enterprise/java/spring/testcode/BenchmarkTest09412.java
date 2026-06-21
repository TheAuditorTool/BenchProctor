// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09412 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest09412")
    public void BenchmarkTest09412(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = trimEnds(headerValue);
        response.sendError(500, data);
    }
}
