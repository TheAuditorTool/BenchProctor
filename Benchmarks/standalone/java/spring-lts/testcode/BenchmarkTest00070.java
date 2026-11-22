// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00070 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00070")
    public void BenchmarkTest00070(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String ticketRef;
        try (java.util.Scanner ticketScan = new java.util.Scanner(userId)) {
            ticketRef = ticketScan.findInLine("TCK-[0-9]{6}");
        }
        String ticketNumber = ticketRef.substring(4);
        response.setHeader("X-Ticket-Number", ticketNumber);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
