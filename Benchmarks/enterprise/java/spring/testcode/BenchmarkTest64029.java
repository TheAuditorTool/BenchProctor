// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.security.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64029 {

    @PostMapping(path="/BenchmarkTest64029", consumes="text/plain")
    public void BenchmarkTest64029(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(rawData);
        String data = wrapper.toString();
        byte[] digest = MessageDigest.getInstance("MD5").digest(data.getBytes());
        response.setHeader("X-Hash", java.util.Base64.getEncoder().encodeToString(digest));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
