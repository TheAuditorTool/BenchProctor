// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16393 {

    @GetMapping("/BenchmarkTest16393")
    public void BenchmarkTest16393(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(envValue);
        String data = normalizer.apply(envValue);
        String encKeyStr = System.getenv("DATA_ENC_KEY");
        long keyExpiresAt = 1577836800L;
        byte[] staleKeyMat = java.security.MessageDigest.getInstance("SHA-256").digest(encKeyStr.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        javax.crypto.SecretKey staleKey = new javax.crypto.spec.SecretKeySpec(java.util.Arrays.copyOf(staleKeyMat, 32), "AES");
        javax.crypto.Cipher staleCipher = javax.crypto.Cipher.getInstance("AES");
        staleCipher.init(javax.crypto.Cipher.ENCRYPT_MODE, staleKey);
        byte[] ct = staleCipher.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        response.setHeader("X-Encrypted-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
