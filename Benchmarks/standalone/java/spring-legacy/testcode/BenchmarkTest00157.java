// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00157 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest00157")
    public void BenchmarkTest00157(@javax.validation.constraints.Size(max = 4096) @RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = normalize(hostValue);
        String cookieValue = java.net.URLEncoder.encode(data, java.nio.charset.StandardCharsets.UTF_8);
        org.springframework.http.ResponseCookie sessionCookie = org.springframework.http.ResponseCookie.from("session", cookieValue).path("/").secure(true).httpOnly(true).sameSite("Strict").build();
        response.addHeader(org.springframework.http.HttpHeaders.SET_COOKIE, sessionCookie.toString());
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
