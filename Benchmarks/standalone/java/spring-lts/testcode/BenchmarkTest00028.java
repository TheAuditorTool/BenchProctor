// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00028 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00028")
    public void BenchmarkTest00028(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("APP_INPUT")).orElse("");
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String data = transform.apply(envValue);
        int quantity = Integer.parseInt(data);
        int orderTotalCents = quantity * 1250;
        if (orderTotalCents > 5_000_000) { response.sendError(422, "order exceeds credit limit"); return; }
        response.setHeader("X-Order-Total", String.valueOf(orderTotalCents));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
