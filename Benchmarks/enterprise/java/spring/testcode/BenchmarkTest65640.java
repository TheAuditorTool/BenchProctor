// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest65640 {

    @PostMapping(path="/BenchmarkTest65640", consumes="multipart/form-data")
    public void BenchmarkTest65640(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + uploadName;
        String data = valueSupplier.get();
        byte[] hashSalt = new byte[16]; new java.security.SecureRandom().nextBytes(hashSalt);
        java.security.MessageDigest hashMd = java.security.MessageDigest.getInstance("SHA-256");
        hashMd.update(hashSalt);
        byte[] digest = hashMd.digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
