// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest08672 {

    @GetMapping("/BenchmarkTest08672")
    public void BenchmarkTest08672(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> originValue)
            .thenApply(v -> java.text.Normalizer.normalize(v, java.text.Normalizer.Form.NFC).strip())
            .join();
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] kv = data.split("=", 2);
        if (kv.length == 2) {
            entity.put(kv[0], kv[1]);
            response.setHeader("X-Field-Set", kv[0]);
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
