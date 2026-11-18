// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00192 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00192")
    public void BenchmarkTest00192(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("APP_INPUT")).orElse("");
        java.util.function.Supplier<String> valueSupplier = () -> envValue.strip();
        String data = valueSupplier.get();
        if (!("true".equals(data) || "false".equals(data))) { response.sendError(400); return; }
        String validatedName = data.matches("[A-Za-z][A-Za-z .'-]{0,63}") ? data.strip() : "guest";
        request.getSession().setAttribute("displayName", validatedName);
        String greetingName = String.valueOf(request.getSession().getAttribute("displayName"));
        response.getWriter().print("{\"greetingLength\":" + greetingName.length() + "}");
    }
}
