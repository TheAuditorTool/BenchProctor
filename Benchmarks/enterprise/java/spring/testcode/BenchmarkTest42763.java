// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest42763 {

    @GetMapping("/BenchmarkTest42763")
    public void BenchmarkTest42763(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "default_setting_value";
        String prefix = secretValue.length() > 0 ? secretValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = secretValue.toLowerCase(); break;
            case "f": data = secretValue.toUpperCase(); break;
            default: data = secretValue.strip(); break;
        }
        if (data == null) throw new IllegalArgumentException("input required");
        java.security.KeyStore ks = java.security.KeyStore.getInstance("PKCS12");
        ks.load(new java.io.FileInputStream("/etc/app/keystore.p12"), "changeit".toCharArray());
        java.security.Key keystoreKey = ks.getKey("api_key", "changeit".toCharArray());
        if (keystoreKey == null) throw new IllegalStateException("api_key not found in keystore");
        String storeCred = java.util.Base64.getEncoder().encodeToString(keystoreKey.getEncoded());
        byte[] encIv = new byte[12]; new java.security.SecureRandom().nextBytes(encIv);
        byte[] keyMaterial = java.security.MessageDigest.getInstance("SHA-256").digest(storeCred.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(java.util.Arrays.copyOf(keyMaterial, 32), "AES");
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/GCM/NoPadding");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.GCMParameterSpec(128, encIv));
        byte[] ct = cipher.doFinal(storeCred.getBytes());
        response.setHeader("X-Encrypted-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
    }
}
