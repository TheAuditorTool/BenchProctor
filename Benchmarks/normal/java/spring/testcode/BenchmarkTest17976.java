// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest17976 {

    private static String toLowerCase(String v) { return v.toLowerCase(); }

    @PostMapping("/BenchmarkTest17976")
    public void BenchmarkTest17976(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = toLowerCase(fieldValue);
        javax.crypto.Mac authMac = javax.crypto.Mac.getInstance("HmacSHA256");
        authMac.init(new javax.crypto.spec.SecretKeySpec(System.getenv("HMAC_SECRET").getBytes(java.nio.charset.StandardCharsets.UTF_8), "HmacSHA256"));
        byte[] presented = authMac.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        byte[] stored = java.util.Base64.getDecoder().decode((String) request.getSession().getAttribute("credHash"));
        if (!java.security.MessageDigest.isEqual(presented, stored)) { response.sendError(401); return; }
        response.getWriter().print("{\"auth\":\"ok\"}");
    }
}
