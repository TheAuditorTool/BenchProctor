// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00236 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @PostMapping(path="/BenchmarkTest00236", consumes="multipart/form-data")
    public void BenchmarkTest00236(@javax.validation.constraints.Size(max = 4096) @RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("[ \\t]+", " ");
        String data = transform.apply(multipartValue);
        int recordCount = Integer.parseInt(data);
        java.nio.ByteBuffer exportBuffer = java.nio.ByteBuffer.allocate(recordCount * 512);
        response.setHeader("X-Export-Capacity", String.valueOf(exportBuffer.capacity()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
