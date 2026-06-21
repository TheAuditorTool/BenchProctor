// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest21980 {

    @PostMapping(path="/BenchmarkTest21980", consumes="text/plain")
    public void BenchmarkTest21980(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(rawData).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
