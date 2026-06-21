// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37261 {

    @GetMapping("/BenchmarkTest37261")
    public void BenchmarkTest37261(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("USER_INPUT")).orElse("");
        java.util.Properties container = new java.util.Properties();
        container.load(new java.io.StringReader("rawValue=" + envValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", container.getProperty("format", "plain"));
        String data = container.getProperty("rawValue", "");
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
