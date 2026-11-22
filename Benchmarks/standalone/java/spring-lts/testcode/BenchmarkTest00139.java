// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00139 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00139", consumes="multipart/form-data")
    public void BenchmarkTest00139(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(uploadName)); }
        catch (NumberFormatException e) { data = uploadName; }
        long randValue = java.util.concurrent.ThreadLocalRandom.current().nextLong() ^ data.hashCode();
        response.setHeader("X-Rand", String.valueOf(randValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
