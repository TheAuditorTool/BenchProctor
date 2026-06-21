// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36115 {

    @GetMapping("/BenchmarkTest36115")
    public void BenchmarkTest36115(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> userId)
            .thenApply(v -> v.strip().toLowerCase())
            .join();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
            response.setHeader("X-Eval-Result", String.valueOf(evalResult));
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
