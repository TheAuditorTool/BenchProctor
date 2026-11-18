// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00356 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00356")
    public void BenchmarkTest00356(@jakarta.validation.constraints.Size(max = 4096) @RequestHeader("X-Forwarded-For") String xForwardedFor, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String forwardedIp = xForwardedFor != null ? xForwardedFor : "";
        String data = String.format("%s", forwardedIp);
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("DESede/CBC/PKCS5Padding");
        byte[] desedeIv = new byte[8]; new java.security.SecureRandom().nextBytes(desedeIv);
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, new javax.crypto.spec.SecretKeySpec(java.util.Base64.getDecoder().decode(java.util.Objects.requireNonNullElse(System.getenv("LEGACY_DESEDE_KEY"), "")), "DESede"), new javax.crypto.spec.IvParameterSpec(desedeIv));
        byte[] ct = cipher.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
