// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest41712 {

    @GetMapping("/BenchmarkTest41712")
    public void BenchmarkTest41712(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = java.util.concurrent.CompletableFuture
            .supplyAsync(() -> uaValue)
            .thenApply(v -> v.strip().replaceAll("\\s+", " "))
            .join();
        if (data == null) throw new IllegalArgumentException("input required");
        io.github.jopenlibs.vault.VaultConfig vc = new io.github.jopenlibs.vault.VaultConfig()
            .address("https://vault.svc.local:8200")
            .token(System.getenv("VAULT_TOKEN"))
            .build();
        io.github.jopenlibs.vault.Vault vault = io.github.jopenlibs.vault.Vault.create(vc);
        String storeCred = vault.logical().read("secret/myapp/db_password").getData().get("password");
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
