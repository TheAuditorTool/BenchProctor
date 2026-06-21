// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23390 {

    @PostMapping("/BenchmarkTest23390")
    public void BenchmarkTest23390(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> fieldValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        byte[] computed = java.security.MessageDigest.getInstance("MD5").digest(data.getBytes());
        String computedHex = java.util.Base64.getEncoder().encodeToString(computed);
        String presented = request.getHeader("X-Signature") != null ? request.getHeader("X-Signature") : "";
        if (!computedHex.equals(presented)) {
            response.sendError(403, "bad signature"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
