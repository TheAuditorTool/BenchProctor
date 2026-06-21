// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18725 {

    @GetMapping("/BenchmarkTest18725")
    public void BenchmarkTest18725(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "p4ssw0rd_test_xyz";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::trim);
        String data = decorated.apply(secretValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, processed).compact();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
