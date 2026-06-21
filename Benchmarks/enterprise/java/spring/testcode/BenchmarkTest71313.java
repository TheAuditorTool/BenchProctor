// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest71313 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    @PostMapping("/BenchmarkTest71313")
    public void BenchmarkTest71313(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        java.util.Properties box = new java.util.Properties();
        box.load(new java.io.StringReader("rawValue=" + jsonValue.replace("\n", " ").replace("\r", " ") + "\nformat=plain\nversion=1"));
        response.setHeader("X-Config-Format", box.getProperty("format", "plain"));
        String data = box.getProperty("rawValue", "");
        byte[] gcmIv = new byte[12]; new java.security.SecureRandom().nextBytes(gcmIv);
        String negotiatedAlgo = "weak".equals(data) ? "DES/ECB/PKCS5Padding" : "AES/GCM/NoPadding";
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance(negotiatedAlgo);
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(new byte[16], "AES");
        if (negotiatedAlgo.startsWith("AES")) {
            cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.GCMParameterSpec(128, gcmIv));
        } else {
            cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, new javax.crypto.spec.SecretKeySpec(new byte[8], "DES"));
        }
        byte[] ct = cipher.doFinal(data.getBytes());
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
