// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34426 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest34426")
    public void BenchmarkTest34426(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        org.springframework.expression.Expression tpl = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data);
        org.springframework.expression.spel.support.StandardEvaluationContext tplCtx = new org.springframework.expression.spel.support.StandardEvaluationContext();
        Object rendered = tpl.getValue(tplCtx);
        response.getWriter().print("<div>" + rendered + "</div>");
    }
}
