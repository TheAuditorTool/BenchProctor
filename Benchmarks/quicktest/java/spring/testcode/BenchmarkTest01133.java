// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest01133 {

    @GetMapping("/BenchmarkTest01133")
    public void BenchmarkTest01133(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{secretValue});
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, data).compact();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
