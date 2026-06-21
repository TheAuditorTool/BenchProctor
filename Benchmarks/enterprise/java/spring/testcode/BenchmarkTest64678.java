// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64678 {

    @PostMapping(path="/BenchmarkTest64678", consumes="multipart/form-data")
    public void BenchmarkTest64678(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(multipartValue);
        String data = envelope.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        org.springframework.expression.Expression tpl = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(processed);
        org.springframework.expression.spel.support.StandardEvaluationContext tplCtx = new org.springframework.expression.spel.support.StandardEvaluationContext();
        Object rendered = tpl.getValue(tplCtx);
        response.getWriter().print("<div>" + rendered + "</div>");
    }
}
