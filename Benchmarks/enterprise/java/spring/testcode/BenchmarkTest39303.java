// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest39303 {

    @GetMapping("/BenchmarkTest39303/{pathId}")
    public void BenchmarkTest39303(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(pathValue, "request");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        javax.crypto.Mac authMac = javax.crypto.Mac.getInstance("HmacSHA256");
        authMac.init(new javax.crypto.spec.SecretKeySpec(System.getenv("HMAC_SECRET").getBytes(java.nio.charset.StandardCharsets.UTF_8), "HmacSHA256"));
        byte[] presented = authMac.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        byte[] stored = java.util.Base64.getDecoder().decode((String) request.getSession().getAttribute("credHash"));
        if (!java.security.MessageDigest.isEqual(presented, stored)) { response.sendError(401); return; }
        response.getWriter().print("{\"auth\":\"ok\"}");
    }
}
