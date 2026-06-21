// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17629 {

    @GetMapping("/BenchmarkTest17629")
    public void BenchmarkTest17629(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> forwardedIp)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        if (data.length() > 2048) { response.sendError(400, "schema invalid"); return; }
        response.sendRedirect(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
