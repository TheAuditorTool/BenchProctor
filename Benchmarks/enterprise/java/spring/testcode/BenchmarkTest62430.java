// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62430 {

    @PostMapping(path="/BenchmarkTest62430", consumes="multipart/form-data")
    public void BenchmarkTest62430(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        if (!("true".equals(multipartValue) || "false".equals(multipartValue))) { response.sendError(400); return; }
        org.springframework.expression.Expression tpl = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(multipartValue);
        org.springframework.expression.spel.support.StandardEvaluationContext tplCtx = new org.springframework.expression.spel.support.StandardEvaluationContext();
        Object rendered = tpl.getValue(tplCtx);
        response.getWriter().print("<div>" + rendered + "</div>");
    }
}
