// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00188 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00188/{pathId}")
    public void BenchmarkTest00188(@javax.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Properties box = new java.util.Properties();
        box.setProperty("value", pathValue);
        String data = box.getProperty("value", "");
        long randValue = java.security.SecureRandom.getInstance("DRBG").nextLong() ^ data.hashCode();
        response.setHeader("X-Rand", String.valueOf(randValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
