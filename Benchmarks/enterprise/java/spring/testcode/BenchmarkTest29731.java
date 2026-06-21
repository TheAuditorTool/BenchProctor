// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest29731 {

    @PostMapping("/BenchmarkTest29731")
    public void BenchmarkTest29731(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> commentValue)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            response.getWriter().print("<div>" + data + "</div>");
        }
    }
}
