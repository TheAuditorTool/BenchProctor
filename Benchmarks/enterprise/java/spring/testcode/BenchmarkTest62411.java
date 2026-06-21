// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62411 {

    @GetMapping("/BenchmarkTest62411")
    public void BenchmarkTest62411(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder payload = new StringBuilder();
        payload.append(headerValue);
        String data = payload.toString();
        response.sendError(500, data);
    }
}
