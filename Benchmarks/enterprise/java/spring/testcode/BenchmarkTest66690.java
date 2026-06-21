// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66690 {

    @GetMapping("/BenchmarkTest66690")
    public void BenchmarkTest66690(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.Map.Entry<String,String> pair = java.util.Map.entry(headerValue, "form");
        response.setHeader("X-Tuple-Context", pair.getValue());
        String data = pair.getKey();
        String forwardedFor = request.getHeader("X-Forwarded-For");
        String clientIp = forwardedFor != null ? forwardedFor : data;
        if ("127.0.0.1".equals(clientIp) || "10.0.0.1".equals(clientIp)) {
            response.getWriter().print("{\"role\":\"admin\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
