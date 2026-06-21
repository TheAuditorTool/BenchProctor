// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest36785 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest36785")
    public void BenchmarkTest36785(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        holder.set(userId);
        String data = holder.get();
        byte[] passwordSalt = new byte[16]; new java.security.SecureRandom().nextBytes(passwordSalt);
        javax.crypto.SecretKeyFactory skf = javax.crypto.SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256");
        byte[] derived = skf.generateSecret(new javax.crypto.spec.PBEKeySpec(data.toCharArray(), passwordSalt, 100000, 256)).getEncoded();
        response.setHeader("X-PBKDF2", java.util.Base64.getEncoder().encodeToString(derived));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
