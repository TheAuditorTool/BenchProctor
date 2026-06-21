// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13000 {

    @GetMapping("/BenchmarkTest13000")
    public void BenchmarkTest13000(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = String.format("%s", authHeader);
        Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
