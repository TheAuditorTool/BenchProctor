// SPDX-License-Identifier: Apache-2.0
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05529 {

    @GetMapping("/BenchmarkTest05529")
    public void BenchmarkTest05529(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "p4ssw0rd_test_xyz";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(secretValue);
        String data = wrapper.toString();
        Jwts.builder().setSubject("user").signWith(SignatureAlgorithm.HS256, data).compact();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
