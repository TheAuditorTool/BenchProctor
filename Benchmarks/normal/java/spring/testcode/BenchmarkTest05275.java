// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05275 {

    @PostMapping(path="/BenchmarkTest05275", consumes="text/plain")
    public void BenchmarkTest05275(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> rawData)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        int divisor = Integer.parseInt(data);
        if (divisor == 0) { response.sendError(400); return; }
        int result = 100 / divisor;
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
