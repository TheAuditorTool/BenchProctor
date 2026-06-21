// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest69640 {

    @GetMapping("/BenchmarkTest69640")
    public void BenchmarkTest69640(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "config_secret_test_abc123";
        java.util.Deque<String> pending = new java.util.ArrayDeque<>(java.util.Arrays.asList(secretValue.split(",")));
        java.util.List<String> lowered = new java.util.ArrayList<>();
        while (!pending.isEmpty()) { lowered.add(pending.poll().toLowerCase()); }
        String data = String.join(",", lowered);
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, data).compact();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
