// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest11278 {

    @GetMapping("/BenchmarkTest11278")
    public void BenchmarkTest11278(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(headerValue);
        String data = envelope.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.sendError(500, processed);
    }
}
