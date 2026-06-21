// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16932 {

    @GetMapping("/BenchmarkTest16932")
    public void BenchmarkTest16932(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "app_display_name";
        String data = String.format("%s", secretValue);
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        byte[] encIv = new byte[12]; new java.security.SecureRandom().nextBytes(encIv);
        byte[] keyMaterial = java.security.MessageDigest.getInstance("SHA-256").digest(storeCred.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(java.util.Arrays.copyOf(keyMaterial, 32), "AES");
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.GCMParameterSpec(128, encIv));
        byte[] ct = cipher.doFinal(storeCred.getBytes());
        response.setHeader("X-Encrypted-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
    }
}
