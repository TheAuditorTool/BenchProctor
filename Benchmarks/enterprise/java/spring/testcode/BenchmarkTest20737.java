// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest20737 {

    @PostMapping(path="/BenchmarkTest20737", consumes="multipart/form-data")
    public void BenchmarkTest20737(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(uploadName);
        int result = 100 / Integer.parseInt(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
