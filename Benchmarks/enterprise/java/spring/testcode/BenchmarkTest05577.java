// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05577 {

    @GetMapping("/BenchmarkTest05577")
    public void BenchmarkTest05577(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> hostValue)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        java.util.Set<String> allowed = java.util.Set.of("ls", "cat", "date", "echo");
        if (!allowed.contains(data)) { response.sendError(403); return; }
        String allowedBin = data;
        System.loadLibrary(allowedBin);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
