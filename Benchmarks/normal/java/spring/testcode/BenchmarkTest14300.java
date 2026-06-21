// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14300 {

    @GetMapping("/BenchmarkTest14300")
    public void BenchmarkTest14300(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> authHeader)
            .thenApply(v -> java.text.Normalizer.normalize(v, java.text.Normalizer.Form.NFC).strip())
            .join();
        response.sendError(500, data);
    }
}
