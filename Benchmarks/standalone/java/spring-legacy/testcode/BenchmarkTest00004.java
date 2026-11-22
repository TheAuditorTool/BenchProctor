// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00004 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00004")
    public void BenchmarkTest00004(@javax.validation.constraints.Size(max = 4096) @RequestHeader("X-Custom-Header") String xCustomHeader, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String headerValue = xCustomHeader != null ? xCustomHeader : "";
        java.util.function.Supplier<String> valueSupplier = () -> headerValue.strip();
        String data = valueSupplier.get();
        String ticketRef;
        try (java.util.Scanner ticketScan = new java.util.Scanner(data)) {
            ticketRef = ticketScan.findInLine("TCK-[0-9]{6}");
        }
        String ticketNumber = ticketRef.substring(4);
        response.setHeader("X-Ticket-Number", ticketNumber);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
