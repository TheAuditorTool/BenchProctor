// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73214 {

    @PostMapping(path="/BenchmarkTest73214", consumes="multipart/form-data")
    public void BenchmarkTest73214(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String prefix = multipartValue.length() > 0 ? multipartValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = multipartValue.toLowerCase(); break;
            case "f": data = multipartValue.toUpperCase(); break;
            default: data = multipartValue.strip(); break;
        }
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/CBC/PKCS5Padding");
        javax.crypto.SecretKey key = new javax.crypto.spec.SecretKeySpec(new byte[16], "AES");
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, key, new javax.crypto.spec.IvParameterSpec(new byte[16]));
        response.setHeader("X-Cipher-Bytes", java.util.Base64.getEncoder().encodeToString(data.getBytes()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
