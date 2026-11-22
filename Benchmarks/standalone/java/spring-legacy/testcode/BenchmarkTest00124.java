// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00124 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    static final class FormData {
        private final String payload;
        FormData(String payload) { this.payload = payload; }
        String getPayload() { return payload; }
    }

    @PostMapping("/BenchmarkTest00124")
    public void BenchmarkTest00124(@javax.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        FormData payload = new FormData(commentValue);
        String data = payload.getPayload();
        try { Integer.parseInt(data); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        int boundedVal = Math.max(0, Math.min(Integer.parseInt(data), 1048576));
        int quantity = boundedVal;
        int orderTotalCents = quantity * 1250;
        if (orderTotalCents > 5_000_000) { response.sendError(422, "order exceeds credit limit"); return; }
        response.setHeader("X-Order-Total", String.valueOf(orderTotalCents));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
