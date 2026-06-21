// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76301 {

    private enum AllowedValue { PLAIN, MARKDOWN, HTML, TEXT }

    @GetMapping("/BenchmarkTest76301")
    public void BenchmarkTest76301(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String prefix = hostValue.length() > 0 ? hostValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = hostValue.toLowerCase(); break;
            case "f": data = hostValue.toUpperCase(); break;
            default: data = hostValue.strip(); break;
        }
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        org.springframework.expression.Expression tpl = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data);
        org.springframework.expression.spel.support.StandardEvaluationContext tplCtx = new org.springframework.expression.spel.support.StandardEvaluationContext();
        Object rendered = tpl.getValue(tplCtx);
        response.getWriter().print("<div>" + rendered + "</div>");
    }
}
