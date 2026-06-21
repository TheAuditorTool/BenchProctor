// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20464 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest20464")
    public void BenchmarkTest20464(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        atomicValue.set(userId);
        String data = atomicValue.get();
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
            response.getWriter().print("<div>" + evaluated + "</div>");
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
    }
}
