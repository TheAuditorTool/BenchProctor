// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest58563 {

    @GetMapping("/BenchmarkTest58563")
    public void BenchmarkTest58563(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(headerValue);
        String data = envelope.toString();
        if (System.currentTimeMillis() > 1000000000000L) {
            Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
            response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
