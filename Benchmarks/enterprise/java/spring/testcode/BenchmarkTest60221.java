// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60221 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @PostMapping(path="/BenchmarkTest60221", consumes="text/plain")
    public void BenchmarkTest60221(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String data = stripCRLF(rawData);
        byte[] randomSalt = new byte[16]; new java.security.SecureRandom().nextBytes(randomSalt);
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(randomSalt);
        byte[] digest = md.digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
