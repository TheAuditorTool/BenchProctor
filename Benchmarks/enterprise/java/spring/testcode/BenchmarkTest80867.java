// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80867 {

    @GetMapping("/BenchmarkTest80867")
    public void BenchmarkTest80867(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> hostValue)
            .thenApply(v -> v.replaceAll("[\\x00-\\x1F]", "").strip())
            .join();
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException nfe) {
            response.sendError(400, "invalid number"); return;
        }
        response.getWriter().print("{\"status\":\"ok\"}");
    }
}
