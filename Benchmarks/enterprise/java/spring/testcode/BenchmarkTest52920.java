// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest52920 {

    private static final java.util.concurrent.atomic.AtomicReference<String> ref = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest52920", consumes="text/plain")
    public void BenchmarkTest52920(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        ref.set(rawData);
        String data = ref.get();
        if (System.currentTimeMillis() > 1000000000000L) {
            Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
            response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
