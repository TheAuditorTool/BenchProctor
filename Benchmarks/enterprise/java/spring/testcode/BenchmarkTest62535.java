// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62535 {

    @GetMapping("/BenchmarkTest62535")
    public void BenchmarkTest62535(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{refererValue});
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        org.springframework.expression.Expression tpl = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data);
        org.springframework.expression.spel.support.StandardEvaluationContext tplCtx = new org.springframework.expression.spel.support.StandardEvaluationContext();
        Object rendered = tpl.getValue(tplCtx);
        response.getWriter().print("<div>" + rendered + "</div>");
    }
}
