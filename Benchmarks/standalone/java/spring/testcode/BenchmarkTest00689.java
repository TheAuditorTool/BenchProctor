// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00689 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00689/{pathId}")
    public void BenchmarkTest00689(@jakarta.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String prefix = pathValue.length() > 0 ? pathValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = pathValue.toLowerCase(); break;
            case "f": data = pathValue.toUpperCase(); break;
            default: data = pathValue.strip(); break;
        }
        if (!("true".equals(data) || "false".equals(data))) { response.sendError(400); return; }
        Object codeResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(data).getValue();
        response.setHeader("X-Code-Result", String.valueOf(codeResult));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
