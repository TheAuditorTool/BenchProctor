// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00094 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    record FormData(String payload) {}

    @GetMapping("/BenchmarkTest00094")
    public void BenchmarkTest00094(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        FormData payload = new FormData(userId);
        String data = payload.payload();
        if (!("true".equals(data) || "false".equals(data))) { response.sendError(400); return; }
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
