// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest39447 {

    @GetMapping("/BenchmarkTest39447")
    public void BenchmarkTest39447(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> uaValue)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        String processed = org.owasp.encoder.Encode.forHtml(data);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
