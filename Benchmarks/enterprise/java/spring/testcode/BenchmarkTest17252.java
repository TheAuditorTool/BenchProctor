// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17252 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @PostMapping("/BenchmarkTest17252")
    public void BenchmarkTest17252(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = "[%s]".formatted(fieldValue);
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
