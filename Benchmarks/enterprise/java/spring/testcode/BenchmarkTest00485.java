// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00485 {

    private static final class ValidatedDto {
        @jakarta.validation.constraints.NotNull
        @jakarta.validation.constraints.Pattern(regexp = "^[A-Za-z0-9_.-]+$")
        @jakarta.validation.constraints.Size(max = 256)
        public String value;
        ValidatedDto(String v) { this.value = v; }
    }
    private static final jakarta.validation.Validator VALIDATOR =
        jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();

    @GetMapping("/BenchmarkTest00485")
    public void BenchmarkTest00485(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", authHeader);
        String data = sw.toString();
        java.util.Set<jakarta.validation.ConstraintViolation<ValidatedDto>> violations = VALIDATOR.validate(new ValidatedDto(data));
        if (!violations.isEmpty()) { response.sendError(400, "schema invalid"); return; }
        String trustedClaim = data;
        response.setHeader("X-Claim-Trusted", trustedClaim);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
