// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60138 {

    private static final class ValidatedDto {
        @jakarta.validation.constraints.NotNull
        @jakarta.validation.constraints.Pattern(regexp = "^[A-Za-z0-9_.-]+$")
        @jakarta.validation.constraints.Size(max = 256)
        public String value;
        ValidatedDto(String v) { this.value = v; }
    }
    private static final jakarta.validation.Validator VALIDATOR =
        jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();

    @GetMapping("/BenchmarkTest60138")
    public void BenchmarkTest60138(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        java.util.Set<jakarta.validation.ConstraintViolation<ValidatedDto>> violations = VALIDATOR.validate(new ValidatedDto(userId));
        if (!violations.isEmpty()) { response.sendError(400, "schema invalid"); return; }
        response.setContentType("text/html");
        response.getWriter().print(userId);
    }
}
