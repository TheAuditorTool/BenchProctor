// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00053 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00053")
    public void BenchmarkTest00053(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("APP_INPUT")).orElse("");
        String data;
        try { data = String.valueOf(Integer.parseInt(envValue)); }
        catch (NumberFormatException e) { data = envValue; }
        try { Double.parseDouble(data); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        String boundedVal = data;
        String displayName = boundedVal.matches("[A-Za-z][A-Za-z .'-]{0,63}") ? boundedVal.strip() : "guest";
        request.getSession().setAttribute("displayName", displayName);
        String greetingName = String.valueOf(request.getSession().getAttribute("displayName"));
        response.getWriter().print("{\"greetingLength\":" + greetingName.length() + "}");
    }
}
