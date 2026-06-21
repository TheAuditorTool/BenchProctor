// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest82952 {

    @GetMapping("/BenchmarkTest82952")
    public void BenchmarkTest82952(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> uaValue)
            .thenApply(v -> java.text.Normalizer.normalize(v, java.text.Normalizer.Form.NFC).strip())
            .join();
        String processed = data.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;");
        response.setHeader("X-Forwarded-For", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
