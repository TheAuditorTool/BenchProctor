// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13886 {

    @GetMapping("/BenchmarkTest13886")
    public void BenchmarkTest13886(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> forwardedIp)
            .thenApply(v -> java.text.Normalizer.normalize(v, java.text.Normalizer.Form.NFC).strip())
            .join();
        String forwardedFor = request.getHeader("X-Forwarded-For");
        String clientIp = forwardedFor != null ? forwardedFor : data;
        if ("127.0.0.1".equals(clientIp) || "10.0.0.1".equals(clientIp)) {
            response.getWriter().print("{\"role\":\"admin\"}");
            return;
        }
        response.sendError(403, "forbidden");
    }
}
