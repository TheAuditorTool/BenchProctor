// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65590 {

    @PostMapping(path="/BenchmarkTest65590", consumes="multipart/form-data")
    public void BenchmarkTest65590(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(multipartValue);
        org.springframework.expression.Expression tpl = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data);
        org.springframework.expression.spel.support.StandardEvaluationContext tplCtx = new org.springframework.expression.spel.support.StandardEvaluationContext();
        Object rendered = tpl.getValue(tplCtx);
        response.getWriter().print("<div>" + rendered + "</div>");
    }
}
