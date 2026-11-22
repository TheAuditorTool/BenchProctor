// SPDX-License-Identifier: Apache-2.0
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;

@RestController
@Validated
public class BenchmarkTest00092 {
    @InitBinder
    public void restrictBinding(WebDataBinder binder) {
        binder.setDisallowedFields("id");
    }

    @ExceptionHandler(Exception.class)
    public ResponseEntity<String> handleFailure(Exception ex) {
        return ResponseEntity.status(500).body("request failed");
    }

    @GetMapping("/BenchmarkTest00092")
    public void BenchmarkTest00092(@javax.validation.constraints.Size(max = 4096) @CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        String data;
        try { data = new String(java.util.Base64.getDecoder().decode(cookieValue), java.nio.charset.StandardCharsets.UTF_8); }
        catch (IllegalArgumentException base64Ex) { data = cookieValue; }
        byte[] dataKey = java.util.Base64.getDecoder().decode(System.getenv("DATA_ENC_KEY"));
        org.bouncycastle.crypto.StreamCipher rc4 = new org.bouncycastle.crypto.engines.RC4Engine();
        rc4.init(true, new org.bouncycastle.crypto.params.KeyParameter(dataKey));
        byte[] plain = data.getBytes(java.nio.charset.StandardCharsets.UTF_8);
        byte[] sealed = new byte[plain.length];
        rc4.processBytes(plain, 0, plain.length, sealed, 0);
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(sealed));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
