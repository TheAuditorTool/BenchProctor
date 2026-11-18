// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00350 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00350")
    public void BenchmarkTest00350(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(uaValue)); }
        catch (NumberFormatException e) { data = uaValue; }
        if (!("true".equals(data) || "false".equals(data))) { response.sendError(400); return; }
        Object codeResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.setHeader("X-Code-Result", String.valueOf(codeResult));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
