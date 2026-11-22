// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00078 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00078")
    public void BenchmarkTest00078(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        try { Integer.parseInt(originValue); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        var boundedVal = Math.max(0, Math.min(Integer.parseInt(originValue), 1048576));
        int quantity = boundedVal;
        int orderTotalCents = quantity * 1250;
        if (orderTotalCents > 5_000_000) { response.sendError(422, "order exceeds credit limit"); return; }
        response.setHeader("X-Order-Total", String.valueOf(orderTotalCents));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
