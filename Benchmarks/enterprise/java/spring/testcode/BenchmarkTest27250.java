// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest27250 {

    @GetMapping("/BenchmarkTest27250")
    public void BenchmarkTest27250(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        String data;
        if (refererValue.length() > 256) { data = refererValue.substring(0, 256); }
        else { data = refererValue; }
        byte[] passwordSalt = new byte[16]; new java.security.SecureRandom().nextBytes(passwordSalt);
        javax.crypto.SecretKeyFactory skf = javax.crypto.SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        byte[] derived = skf.generateSecret(new javax.crypto.spec.PBEKeySpec(data.toCharArray(), passwordSalt, 100000, 256)).getEncoded();
        response.setHeader("X-PBKDF2", java.util.Base64.getEncoder().encodeToString(derived));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
