// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13834 {

    @GetMapping("/BenchmarkTest13834")
    public void BenchmarkTest13834(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> refererValue)
            .thenApply(v -> v.length() > 256 ? v.substring(0, 256).strip() : v.strip())
            .join();
        String normalizedPath = java.nio.file.Paths.get(data).normalize().toString();
        Files.write(Paths.get("/var/uploads/" + normalizedPath), "data".getBytes());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
