// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest47600 {

    @GetMapping("/BenchmarkTest47600")
    public void BenchmarkTest47600(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        java.util.List<String> tokens = java.util.Arrays.asList(dotenvValue.split(","));
        String data = String.join(",", tokens);
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/GCM/NoPadding");
        byte[] key = new byte[32]; new java.security.SecureRandom().nextBytes(key);
        byte[] gcmIv = new byte[12]; new java.security.SecureRandom().nextBytes(gcmIv);
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, new javax.crypto.spec.SecretKeySpec(key, "AES"), new javax.crypto.spec.GCMParameterSpec(128, gcmIv));
        byte[] ct = cipher.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.enc")) {
            fw.write(java.util.Base64.getEncoder().encodeToString(ct));
        }
    }
}
