// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest66443 {

    private static final java.util.concurrent.atomic.AtomicReference<String> holder = new java.util.concurrent.atomic.AtomicReference<>();

    @PostMapping(path="/BenchmarkTest66443", consumes="multipart/form-data")
    public void BenchmarkTest66443(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        holder.set(multipartValue);
        String data = holder.get();
        javax.crypto.Cipher cipher = javax.crypto.Cipher.getInstance("AES/GCM/NoPadding");
        byte[] key = new byte[32];
        new java.security.SecureRandom().nextBytes(key);
        byte[] gcmIv = new byte[12]; new java.security.SecureRandom().nextBytes(gcmIv);
        cipher.init(javax.crypto.Cipher.ENCRYPT_MODE, new javax.crypto.spec.SecretKeySpec(key, "AES"), new javax.crypto.spec.GCMParameterSpec(128, gcmIv));
        Files.write(Paths.get("/var/uploads/data.enc"), cipher.doFinal(data.getBytes()));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
