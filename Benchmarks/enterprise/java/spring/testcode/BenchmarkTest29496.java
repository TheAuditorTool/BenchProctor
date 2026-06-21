// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest29496 {

    private static final java.util.concurrent.Semaphore RATE_LIMITER = new java.util.concurrent.Semaphore(10);

    @GetMapping("/BenchmarkTest29496")
    public void BenchmarkTest29496(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder payload = new StringBuilder();
        payload.append(headerValue);
        String data = payload.toString();
        if (!RATE_LIMITER.tryAcquire(1, java.util.concurrent.TimeUnit.SECONDS)) {
            response.sendError(429, "rate limited");
            return;
        }
        try {
            byte[] buf = new byte[Math.min(Integer.parseInt(data), 1048576)];
        } finally { RATE_LIMITER.release(); }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
