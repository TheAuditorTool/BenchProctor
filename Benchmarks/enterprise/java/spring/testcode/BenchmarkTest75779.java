// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75779 {

    @GetMapping("/BenchmarkTest75779/{pathId}")
    public void BenchmarkTest75779(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + pathValue;
        String data = valueSupplier.get();
        if (org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication() == null
                || !org.springframework.security.core.context.SecurityContextHolder.getContext().getAuthentication().isAuthenticated()) {
            response.sendError(401, "not authenticated"); return;
        }
        javax.crypto.Mac mac = javax.crypto.Mac.getInstance("HmacSHA256");
        mac.init(new javax.crypto.spec.SecretKeySpec(System.getenv("HMAC_KEY").getBytes(), "HmacSHA256"));
        byte[] computed = mac.doFinal(data.getBytes());
        byte[] presented = request.getHeader("X-Signature") != null ? request.getHeader("X-Signature").getBytes() : new byte[0];
        if (!java.security.MessageDigest.isEqual(presented, computed)) {
            response.sendError(403, "bad signature"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
