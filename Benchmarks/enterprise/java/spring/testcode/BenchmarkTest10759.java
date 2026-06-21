// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10759 {

    @GetMapping("/BenchmarkTest10759")
    public void BenchmarkTest10759(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        byte[] computed = java.security.MessageDigest.getInstance("MD5").digest(authHeader.getBytes());
        String computedHex = java.util.Base64.getEncoder().encodeToString(computed);
        String presented = request.getHeader("X-Signature") != null ? request.getHeader("X-Signature") : "";
        if (!computedHex.equals(presented)) {
            response.sendError(403, "bad signature"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
