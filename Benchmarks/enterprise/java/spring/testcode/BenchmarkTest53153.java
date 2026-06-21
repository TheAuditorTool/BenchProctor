// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53153 {
    private static class GraphQLRequest {
        public String query;
        public java.util.Map<String, Object> variables;
        public GraphQLRequest() {}
    }

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest53153", consumes="application/json")
    public void BenchmarkTest53153(@RequestBody GraphQLRequest req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String graphqlVar = (req != null && req.variables != null ? String.valueOf(req.variables.get("payload")) : "");
        String data = normalize(graphqlVar);
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
