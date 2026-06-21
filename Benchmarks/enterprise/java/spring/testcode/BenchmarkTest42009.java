// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest42009 {

    @PostMapping("/BenchmarkTest42009")
    public void BenchmarkTest42009(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> commentValue)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        java.nio.file.Path resolvedBase = java.nio.file.Paths.get("/var/app/data").toAbsolutePath();
        java.nio.file.Path requested = resolvedBase.resolve(data).normalize();
        if (!requested.startsWith(resolvedBase)) { response.sendError(403, "outside safe scope"); return; }
        Runtime.getRuntime().exec(new String[]{"chown", "appuser:appgroup", requested.toString()}).waitFor(5, java.util.concurrent.TimeUnit.SECONDS);
    }
}
