// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00127 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00127")
    public void BenchmarkTest00127(@jakarta.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : cookieValue.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        java.util.Map<String, Object> sessionProfile = (java.util.Map<String, Object>) request.getSession().getAttribute("profile");
        if (sessionProfile == null) {
            sessionProfile = new java.util.concurrent.ConcurrentHashMap<>();
            request.getSession().setAttribute("profile", sessionProfile);
        }
        sessionProfile.putAll(java.util.Map.of("displayName", data));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
