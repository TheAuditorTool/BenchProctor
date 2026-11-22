// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00050 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping("/BenchmarkTest00050")
    public void BenchmarkTest00050(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        java.util.Properties holder = new java.util.Properties();
        holder.setProperty("value", fieldValue);
        String data = holder.getProperty("value", "");
        java.util.Map<String, String> regionEndpoints = java.util.Map.of("us-east", "https://us-east.api.svc.local", "eu-west", "https://eu-west.api.svc.local");
        String regionEndpoint = regionEndpoints.get(data);
        if (regionEndpoint == null) { response.sendError(404, "unknown region"); return; }
        boolean secureEndpoint = regionEndpoint.startsWith("https://");
        response.setHeader("X-Region-Secure", String.valueOf(secureEndpoint));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
