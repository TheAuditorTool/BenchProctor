// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49591 {

    @PostMapping("/BenchmarkTest49591")
    public void BenchmarkTest49591(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> fieldValue)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
