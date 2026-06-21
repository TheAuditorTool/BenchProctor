// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04346 {

    @PostMapping("/BenchmarkTest04346")
    public void BenchmarkTest04346(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> commentValue)
            .thenApply(v -> java.text.Normalizer.normalize(v, java.text.Normalizer.Form.NFC).strip())
            .join();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.setHeader("Refresh", "0; url=" + processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
