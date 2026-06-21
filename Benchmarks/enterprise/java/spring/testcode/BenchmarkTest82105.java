// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest82105 {

    private static final java.util.concurrent.atomic.AtomicReference<String> valueRef = new java.util.concurrent.atomic.AtomicReference<>();

    @GetMapping("/BenchmarkTest82105")
    public void BenchmarkTest82105(@RequestHeader("Host") String host, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        valueRef.set(hostValue);
        String data = valueRef.get();
        byte[] digest = MessageDigest.getInstance("MD5").digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
