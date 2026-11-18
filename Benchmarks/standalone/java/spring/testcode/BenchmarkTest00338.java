// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.Cookie;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00338 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00338")
    public void BenchmarkTest00338(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String cookieValue = java.net.URLEncoder.encode(forwardedIp, java.nio.charset.StandardCharsets.UTF_8);
        response.addHeader("Set-Cookie", "session=" + cookieValue + "; Path=/; HttpOnly; SameSite=Strict");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
