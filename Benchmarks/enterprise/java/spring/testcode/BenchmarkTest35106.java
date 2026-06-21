// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest35106 {

    private static final java.util.concurrent.Semaphore RATE_LIMITER = new java.util.concurrent.Semaphore(10);

    @GetMapping("/BenchmarkTest35106")
    public void BenchmarkTest35106(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + authHeader.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
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
