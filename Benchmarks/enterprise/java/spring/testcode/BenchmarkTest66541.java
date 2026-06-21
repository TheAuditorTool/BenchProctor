// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66541 {

    @GetMapping("/BenchmarkTest66541")
    public void BenchmarkTest66541(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String prefix = originValue.length() > 0 ? originValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = originValue.toLowerCase(); break;
            case "f": data = originValue.toUpperCase(); break;
            default: data = originValue.strip(); break;
        }
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
