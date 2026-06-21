// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75189 {

    @GetMapping("/BenchmarkTest75189")
    public void BenchmarkTest75189(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> refererValue)
            .thenApply(v -> v.replace("\t", " ").strip())
            .join();
        if (System.currentTimeMillis() > 1000000000000L) {
            org.springframework.expression.Expression tpl = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data);
            org.springframework.expression.spel.support.StandardEvaluationContext tplCtx = new org.springframework.expression.spel.support.StandardEvaluationContext();
            Object rendered = tpl.getValue(tplCtx);
            response.getWriter().print("<div>" + rendered + "</div>");
        }
    }
}
