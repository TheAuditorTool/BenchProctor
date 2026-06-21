// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest58093 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest58093")
    public void BenchmarkTest58093(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = normalize(originValue);
        java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
        byte[] hashed = md.digest(data.getBytes());
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(java.util.Base64.getEncoder().encodeToString(hashed));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
