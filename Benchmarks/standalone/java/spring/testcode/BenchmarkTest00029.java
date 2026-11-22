// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00029 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00029", consumes="multipart/form-data")
    public void BenchmarkTest00029(@jakarta.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(multipartValue.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        java.util.Map<String, String> regionEndpoints = java.util.Map.of("us-east", "https://us-east.api.svc.local", "eu-west", "https://eu-west.api.svc.local");
        String regionEndpoint = regionEndpoints.get(data);
        if (regionEndpoint == null) { response.sendError(404, "unknown region"); return; }
        boolean secureEndpoint = regionEndpoint.startsWith("https://");
        response.setHeader("X-Region-Secure", String.valueOf(secureEndpoint));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
