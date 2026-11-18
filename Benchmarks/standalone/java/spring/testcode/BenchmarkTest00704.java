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
public class BenchmarkTest00704 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00704", consumes="multipart/form-data")
    public void BenchmarkTest00704(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : uploadName.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        java.util.Random rng = new java.util.Random();
        int randValue = rng.nextInt() ^ data.hashCode();
        response.setHeader("X-Rand", String.valueOf(randValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
