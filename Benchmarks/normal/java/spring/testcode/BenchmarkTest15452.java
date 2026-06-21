// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15452 {

    private static final java.util.concurrent.Semaphore RATE_LIMITER = new java.util.concurrent.Semaphore(10);

    @PostMapping("/BenchmarkTest15452")
    public void BenchmarkTest15452(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(fieldValue, "header");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
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
