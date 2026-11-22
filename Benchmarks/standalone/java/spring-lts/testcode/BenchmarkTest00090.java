// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00090 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00090", consumes="text/plain")
    public void BenchmarkTest00090(@jakarta.validation.constraints.Size(max = 4096) @RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        try { Double.parseDouble(rawData); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        String boundedVal = rawData;
        request.getServletContext().setAttribute("siteBanner", boundedVal);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
