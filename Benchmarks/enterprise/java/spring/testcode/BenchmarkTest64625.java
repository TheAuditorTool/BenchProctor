// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64625 {

    @GetMapping("/BenchmarkTest64625")
    public void BenchmarkTest64625(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> hostValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        if (!data.matches("^[\\w\\s.,;:_/\\-=]+$")) {
            response.sendError(400, "forbidden"); return;
        }
        response.addCookie(new Cookie("session", data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
