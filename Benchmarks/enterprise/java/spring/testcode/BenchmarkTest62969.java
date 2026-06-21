// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62969 {

    @GetMapping("/BenchmarkTest62969")
    public void BenchmarkTest62969(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/CBC/PKCS5Padding");
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(new byte[16], "AES");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.IvParameterSpec(new byte[16]));
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(hostValue.getBytes()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
