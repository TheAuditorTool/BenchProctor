// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78911 {

    @GetMapping("/BenchmarkTest78911")
    public void BenchmarkTest78911(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String argValue = java.util.Optional.ofNullable(System.getProperty("argv.value", "")).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> argValue)
            .thenApply(v -> v.replaceAll("[\\x00-\\x1F]", "").strip())
            .join();
        String normalizedPath = java.nio.file.Paths.get(data).normalize().toString();
        Files.delete(Paths.get("/var/app/data/" + normalizedPath));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
