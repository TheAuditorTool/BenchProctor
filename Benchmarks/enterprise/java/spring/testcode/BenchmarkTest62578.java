// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62578 {

    private static String trimEnds(String v) { return v.trim(); }

    @GetMapping("/BenchmarkTest62578")
    public void BenchmarkTest62578(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = trimEnds(userId);
        java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
        byte[] hashed = md.digest(data.getBytes());
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(java.util.Base64.getEncoder().encodeToString(hashed));
        }
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
