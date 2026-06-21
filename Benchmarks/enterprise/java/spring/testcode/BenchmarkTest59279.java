// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest59279 {

    @GetMapping("/BenchmarkTest59279")
    public void BenchmarkTest59279(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "default_config_label";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(secretValue);
        String data = wrapper.toString();
        if (data == null) throw new IllegalArgumentException("input required");
        java.security.KeyStore ks = java.security.KeyStore.getInstance("PKCS12");
        ks.load(new java.io.FileInputStream("/etc/app/keystore.p12"), "changeit".toCharArray());
        java.security.Key keystoreKey = ks.getKey("api_key", "changeit".toCharArray());
        if (keystoreKey == null) throw new IllegalStateException("api_key not found in keystore");
        String storeCred = java.util.Base64.getEncoder().encodeToString(keystoreKey.getEncoded());
        String secret = storeCred;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, secret).compact();
        response.getWriter().print("{\"signed\":\"ok\"}");
    }
}
