// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest02656 {

    @PostMapping(path="/BenchmarkTest02656", consumes="multipart/form-data")
    public void BenchmarkTest02656(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(uploadName, "http");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        byte[] digest = MessageDigest.getInstance("MD5").digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
