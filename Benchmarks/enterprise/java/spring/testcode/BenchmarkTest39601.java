// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest39601 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    private static String normalize(String v) { return v.strip(); }

    @PostMapping("/BenchmarkTest39601")
    public void BenchmarkTest39601(@Valid @RequestBody UserInput req, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        String data = normalize(jsonValue);
        byte[] staticSalt = "bench_static_1234".getBytes();
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(staticSalt);
        byte[] digest = md.digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
