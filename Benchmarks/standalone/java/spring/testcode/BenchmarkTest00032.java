// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00032 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00032")
    public void BenchmarkTest00032(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        try { Integer.parseInt(cookieValue); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        var boundedVal = Math.max(0, Math.min(Integer.parseInt(cookieValue), 1048576));
        long requested = boundedVal;
        long allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
