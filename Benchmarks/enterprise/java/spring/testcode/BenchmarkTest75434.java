// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75434 {

    @GetMapping("/BenchmarkTest75434")
    public void BenchmarkTest75434(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadedName = java.util.Optional.ofNullable((String) request.getAttribute("uploadName")).orElse("");
        java.util.concurrent.CompletableFuture<String> fut = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> uploadedName)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "));
        String data = fut.get(5, java.util.concurrent.TimeUnit.SECONDS);
        String dispatchKey = "primary";
        if (dispatchKey.equals("primary")) {
            Files.delete(Paths.get("/var/app/data/" + data));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
