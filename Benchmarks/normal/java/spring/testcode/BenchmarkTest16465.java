// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16465 {

    @GetMapping("/BenchmarkTest16465")
    public void BenchmarkTest16465(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "app_display_name";
        StringBuilder carrier = new StringBuilder();
        carrier.append(secretValue);
        String data = carrier.toString();
        if (data == null) throw new IllegalArgumentException("input required");
        String envSecret = System.getenv("APP_SECRET");
        if (envSecret == null) throw new IllegalStateException("APP_SECRET unset");
        String storeCred = envSecret;
        String secret = storeCred;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, secret).compact();
        response.getWriter().print("{\"signed\":\"ok\"}");
    }
}
