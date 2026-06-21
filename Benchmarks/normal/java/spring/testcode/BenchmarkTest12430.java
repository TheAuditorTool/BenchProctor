// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12430 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest12430.class);

    @GetMapping("/BenchmarkTest12430")
    public void BenchmarkTest12430(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> userId)
            .thenApply(v -> v.length() > 256 ? v.substring(0, 256).strip() : v.strip())
            .join();
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        LOG.info("Action: {}", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
