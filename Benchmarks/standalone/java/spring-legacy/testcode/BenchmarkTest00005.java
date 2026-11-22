// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00005 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00005/{pathId}")
    public void BenchmarkTest00005(@javax.validation.constraints.Size(max = 4096) @PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String data;
        if (pathValue.length() > 256) { data = pathValue.substring(0, 256); }
        else { data = pathValue; }
        String ticketRef;
        try (java.util.Scanner ticketScan = new java.util.Scanner(data)) {
            ticketRef = ticketScan.findInLine("TCK-[0-9]{6}");
        }
        if (ticketRef == null) { response.sendError(400, "no ticket reference"); return; }
        String ticketNumber = ticketRef.substring(4);
        response.setHeader("X-Ticket-Number", ticketNumber);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
