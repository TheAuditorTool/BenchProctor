// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01972 {

    @PostMapping("/BenchmarkTest01972")
    public void BenchmarkTest01972(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + commentValue;
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
