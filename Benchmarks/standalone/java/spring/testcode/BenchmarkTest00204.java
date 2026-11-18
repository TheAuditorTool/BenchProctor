// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00204 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00204")
    public void BenchmarkTest00204(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String envValue = java.util.Optional.ofNullable(System.getenv("APP_INPUT")).orElse("");
        String data = String.join(" ", envValue.split("[ \\t]+"));
        byte[] gcmIv = new byte[12]; new java.security.SecureRandom().nextBytes(gcmIv);
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/GCM/NoPadding");
        javax.crypto.KeyGenerator keyGen = javax.crypto.KeyGenerator.getInstance("AES");
        keyGen.init(256);
        javax.crypto.SecretKey key = keyGen.generateKey();
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.GCMParameterSpec(128, gcmIv));
        byte[] ct = cipher.doFinal(data.getBytes());
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
