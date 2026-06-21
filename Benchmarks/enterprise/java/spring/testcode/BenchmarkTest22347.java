// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest22347 {

    @PostMapping(path="/BenchmarkTest22347", consumes="application/xml")
    public void BenchmarkTest22347(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        byte[] raw = xmlValue.getBytes(java.nio.charset.StandardCharsets.ISO_8859_1);
        String data = new String(raw, java.nio.charset.StandardCharsets.UTF_8);
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
