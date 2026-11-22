// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00037 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00037")
    public void BenchmarkTest00037(@jakarta.validation.constraints.Size(max = 4096) @RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        try { Integer.parseInt(userId); }
        catch (NumberFormatException e) { response.sendError(400); return; }
        var boundedVal = Math.max(0, Math.min(Integer.parseInt(userId), 1048576));
        int recordCount = boundedVal;
        java.nio.ByteBuffer exportBuffer = java.nio.ByteBuffer.allocate(recordCount * 512);
        response.setHeader("X-Export-Capacity", String.valueOf(exportBuffer.capacity()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
