// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest50998 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest50998")
    public void BenchmarkTest50998(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = trimEnds(authHeader);
        if (!"test".equals(System.getenv("APP_ENV"))) {
            Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
            response.getWriter().print("<div>" + evaluated + "</div>");
        }
    }
}
