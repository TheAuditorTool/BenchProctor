// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest30117 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest30117")
    public void BenchmarkTest30117(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        byte[] staticSalt = "bench_static_1234".getBytes();
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(staticSalt);
        byte[] digest = md.digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
