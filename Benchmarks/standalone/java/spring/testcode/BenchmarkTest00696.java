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
public class BenchmarkTest00696 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    record FormData(String payload) {}

    @PostMapping(path="/BenchmarkTest00696", consumes="multipart/form-data")
    public void BenchmarkTest00696(@jakarta.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        FormData payload = new FormData(multipartValue);
        String data = payload.payload();
        String cookieValue = java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8);
        response.addHeader("Set-Cookie", "session=" + cookieValue + "; Path=/; Secure; HttpOnly; SameSite=Strict");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
