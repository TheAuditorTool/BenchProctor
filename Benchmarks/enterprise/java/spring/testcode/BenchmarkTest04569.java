// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest04569 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest04569")
    public void BenchmarkTest04569(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "default_setting_value";
        String data = normalize(secretValue);
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        String secret = storeCred;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, secret).compact();
        response.getWriter().print("{\"signed\":\"ok\"}");
    }
}
