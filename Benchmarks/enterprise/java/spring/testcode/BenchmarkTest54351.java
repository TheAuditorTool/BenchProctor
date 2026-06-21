// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest54351 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest54351.class);

    @GetMapping("/BenchmarkTest54351")
    public void BenchmarkTest54351(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String yamlValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.yaml")))).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> yamlValue)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
