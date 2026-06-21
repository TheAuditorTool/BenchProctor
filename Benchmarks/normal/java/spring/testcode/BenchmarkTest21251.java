// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest21251 {

    private static final class ValidatedDto {
        @jakarta.validation.constraints.NotNull
        @jakarta.validation.constraints.Pattern(regexp = "^[A-Za-z0-9_.-]+$")
        @jakarta.validation.constraints.Size(max = 256)
        public String value;
        ValidatedDto(String v) { this.value = v; }
    }
    private static final jakarta.validation.Validator VALIDATOR =
        jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();

    @PostMapping("/BenchmarkTest21251")
    public void BenchmarkTest21251(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Set<jakarta.validation.ConstraintViolation<ValidatedDto>> violations = VALIDATOR.validate(new ValidatedDto(fieldValue));
        if (!violations.isEmpty()) { response.sendError(400, "schema invalid"); return; }
        Object evalResult = new org.springframework.expression.spel.standard.SpelExpressionParser().parseExpression(fieldValue).getValue();
        response.setHeader("X-Eval-Result", String.valueOf(evalResult));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
