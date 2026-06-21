// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18103 {

    static class FormData {
        public String payload;
        public FormData(String payload) { this.payload = payload; }
    }

    @GetMapping("/BenchmarkTest18103")
    public void BenchmarkTest18103(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "AKIAIOSFODNN7EXAMPLE";
        FormData payload = new FormData(secretValue);
        String data = payload.payload;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, data).compact();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
