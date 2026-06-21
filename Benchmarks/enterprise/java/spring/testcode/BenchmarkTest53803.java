// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53803 {

    @GetMapping("/BenchmarkTest53803")
    public void BenchmarkTest53803(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(originValue).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
