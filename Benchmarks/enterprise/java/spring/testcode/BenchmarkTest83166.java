// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest83166 {

    @GetMapping("/BenchmarkTest83166")
    public void BenchmarkTest83166(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> headerValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "))
            .join();
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
