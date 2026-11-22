// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00038 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping("/BenchmarkTest00038")
    public void BenchmarkTest00038(@javax.validation.constraints.Size(max = 4096) @RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String data = commentValue.replace("\u0000", "");
        int quantity = Integer.parseInt(data);
        int orderTotalCents = quantity * 1250;
        if (orderTotalCents > 5_000_000) { response.sendError(422, "order exceeds credit limit"); return; }
        response.setHeader("X-Order-Total", String.valueOf(orderTotalCents));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
