// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest24517 {

    private enum AllowedValue { NOOP, IDENTITY, PASSTHROUGH, ECHO }

    @GetMapping("/BenchmarkTest24517")
    public void BenchmarkTest24517(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        try { AllowedValue.valueOf(uaValue.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { uaValue = AllowedValue.values()[0].name().toLowerCase(); }
        Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(uaValue).getValue();
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
