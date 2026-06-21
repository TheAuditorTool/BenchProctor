// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60306 {

    @PostMapping("/BenchmarkTest60306")
    public void BenchmarkTest60306(@RequestParam("comment") String commentText, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String commentValue = java.util.Optional.ofNullable(commentText).orElse("");
        String prefix = commentValue.length() > 0 ? commentValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = commentValue.toLowerCase(); break;
            case "f": data = commentValue.toUpperCase(); break;
            default: data = commentValue.strip(); break;
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
