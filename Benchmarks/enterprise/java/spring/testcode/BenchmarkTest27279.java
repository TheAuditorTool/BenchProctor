// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest27279 {

    @PostMapping(path="/BenchmarkTest27279", consumes="text/plain")
    public void BenchmarkTest27279(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> rawData)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.sendError(500, processed);
    }
}
