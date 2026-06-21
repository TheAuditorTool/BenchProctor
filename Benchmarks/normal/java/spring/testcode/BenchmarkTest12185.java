// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12185 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }
    private static final byte[] STATIC_IV = new byte[12];

    @GetMapping("/BenchmarkTest12185")
    public void BenchmarkTest12185(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = stripCRLF(authHeader);
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/GCM/NoPadding");
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(new byte[16], "AES");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.GCMParameterSpec(128, STATIC_IV));
        byte[] ct = cipher.doFinal(data.getBytes());
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(ct));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
