// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15331 {

    @GetMapping("/BenchmarkTest15331")
    public void BenchmarkTest15331(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        if (!uaValue.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        Object evaluated = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(uaValue).getValue();
        response.getWriter().print("<div>" + evaluated + "</div>");
    }
}
