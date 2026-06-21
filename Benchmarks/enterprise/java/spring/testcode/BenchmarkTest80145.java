// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80145 {

    @PostMapping(path="/BenchmarkTest80145", consumes="text/plain")
    public void BenchmarkTest80145(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> rawData)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        new java.io.File("/tmp/" + data).createNewFile();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
