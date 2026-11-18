// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00058 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest00058")
    public void BenchmarkTest00058(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = normalize(uaValue);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
