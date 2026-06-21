// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18298 {

    @GetMapping("/BenchmarkTest18298")
    public void BenchmarkTest18298(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.Properties box = new java.util.Properties();
        box.load(new java.io.StringReader("rawValue=" + cookieValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", box.getProperty("format", "plain"));
        String data = box.getProperty("rawValue", "");
        java.security.KeyPairGenerator kpg = java.security.KeyPairGenerator.getInstance("RSA");
        kpg.initialize(2048);
        java.security.KeyPair kp = kpg.generateKeyPair();
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("RSA/ECB/PKCS1Padding");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, kp.getPublic());
        byte[] ptBytes = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] ptSlice = java.util.Arrays.copyOf(ptBytes, Math.min(ptBytes.length, 190));
        byte[] ct = cipher.doFinal(ptSlice);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
