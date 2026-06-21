// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01221 {

    @PostMapping(path="/BenchmarkTest01221", consumes="multipart/form-data")
    public void BenchmarkTest01221(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.function.Consumer<String> lengthGuard = s -> { if (s.length() > 8192) throw new IllegalArgumentException("input too long"); };
        java.util.function.Function<String, String> normalizer = s -> s.strip().replaceAll("\\s+", " ");
        lengthGuard.accept(multipartValue);
        String data = normalizer.apply(multipartValue);
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        long keyExpiresAt = 4102444800L;
        byte[] activeKeyBytes = keyExpiresAt > (System.currentTimeMillis() / 1000L)
            ? storeCred.getBytes(java.nio.charset.StandardCharsets.UTF_8)
            : System.getenv("DATA_ENC_KEY_CURRENT").getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] activeKeyMat = java.security.MessageDigest.getInstance("SHA-256").digest(activeKeyBytes);
        javax.crypto.SecretKey activeKey = new javax.crypto.spec.SecretKeySpec(java.util.Arrays.copyOf(activeKeyMat, 32), "AES");
        javax.crypto.Cipher activeCipher = javax.crypto.Cipher.getInstance("AES");
        activeCipher.init(javax.crypto.Cipher.ENCRYPT_MODE, activeKey);
        byte[] ct = activeCipher.doFinal(storeCred.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        response.setHeader("X-Encrypted-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
    }
}
