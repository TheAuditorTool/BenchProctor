// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62197 {

    @PostMapping(path="/BenchmarkTest62197", consumes="multipart/form-data")
    public void BenchmarkTest62197(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(multipartValue, "cookie");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        javax.crypto.Mac authMac = javax.crypto.Mac.getInstance("HmacSHA256");
        authMac.init(new javax.crypto.spec.SecretKeySpec(System.getenv("HMAC_SECRET").getBytes(java.nio.charset.StandardCharsets.UTF_8), "HmacSHA256"));
        byte[] presented = authMac.doFinal(data.getBytes(java.nio.charset.StandardCharsets.UTF_8));
        byte[] stored = java.util.Base64.getDecoder().decode((String) request.getSession().getAttribute("credHash"));
        if (!java.security.MessageDigest.isEqual(presented, stored)) { response.sendError(401); return; }
        response.getWriter().print("{\"auth\":\"ok\"}");
    }
}
