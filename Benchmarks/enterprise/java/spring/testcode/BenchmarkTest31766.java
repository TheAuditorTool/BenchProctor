// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest31766 {

    @GetMapping("/BenchmarkTest31766")
    public void BenchmarkTest31766(@RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(headerValue).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
