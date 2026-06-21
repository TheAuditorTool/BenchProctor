// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest46637 {

    @GetMapping("/BenchmarkTest46637")
    public void BenchmarkTest46637(@RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String prefix = forwardedIp.length() > 0 ? forwardedIp.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = forwardedIp.toLowerCase(); break;
            case "f": data = forwardedIp.toUpperCase(); break;
            default: data = forwardedIp.strip(); break;
        }
        byte[] hashSalt = new byte[16]; new java.security.SecureRandom().nextBytes(hashSalt);
        java.security.MessageDigest hashMd = java.security.MessageDigest.getInstance("SHA-256");
        hashMd.update(hashSalt);
        byte[] digest = hashMd.digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
