// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest51066 {

    @GetMapping("/BenchmarkTest51066")
    public void BenchmarkTest51066(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> refererValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        int boundedVal;
        try { boundedVal = Integer.parseInt(data); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        if (boundedVal < 0 || boundedVal > 1048576) { response.sendError(400); return; }
        long requested = boundedVal;
        long allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
