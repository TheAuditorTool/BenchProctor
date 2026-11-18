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
public class BenchmarkTest00013 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00013")
    public void BenchmarkTest00013(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", cookieValue);
        String data = box.getProperty("value", "");
        String setCookieValue = java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8);
        response.addHeader("Set-Cookie", "session=" + setCookieValue + "; Path=/; HttpOnly; SameSite=Strict");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
