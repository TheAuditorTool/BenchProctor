// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75836 {

    private static final java.util.concurrent.atomic.AtomicReference<String> stateBox = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest75836", consumes="text/plain")
    public void BenchmarkTest75836(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        stateBox.set(rawData);
        String data = stateBox.get();
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
            response.getWriter().print("<div>" + evaluated + "</div>");
        }
    }
}
