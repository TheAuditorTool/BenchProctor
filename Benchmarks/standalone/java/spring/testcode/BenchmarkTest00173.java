// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00173 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00173")
    public void BenchmarkTest00173(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.format("%s", hostValue);
        record SchemaInput(@jakarta.validation.constraints.Pattern(regexp = "^[a-zA-Z0-9 _.\\-]+$") String value) {}
        jakarta.validation.Validator schemaValidator = jakarta.validation.Validation.buildDefaultValidatorFactory().getValidator();
        if (!schemaValidator.validate(new SchemaInput(data)).isEmpty()) { response.sendError(400, "schema invalid"); return; }
        String validatedName = data.matches("[A-Za-z][A-Za-z .'-]{0,63}") ? data.strip() : "guest";
        request.getSession().setAttribute("displayName", validatedName);
        String greetingName = String.valueOf(request.getSession().getAttribute("displayName"));
        response.getWriter().print("{\"greetingLength\":" + greetingName.length() + "}");
    }
}
