// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38591 {

    private static String stripCRLF(String v) { return v.replace("\r", "").replace("\n", ""); }

    @PostMapping("/BenchmarkTest38591")
    public void BenchmarkTest38591(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String data = stripCRLF(fieldValue);
        java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
        String hashedCred = java.util.Base64.getEncoder().encodeToString(md.digest(data.getBytes(java.nio.charset.StandardCharsets.UTF_8)));
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", hashedCred)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
