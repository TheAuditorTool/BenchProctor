// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23039 {

    private static String normalize(String v) { return v.strip(); }

    @GetMapping("/BenchmarkTest23039")
    public void BenchmarkTest23039(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "p4ssw0rd_test_xyz";
        String data = normalize(secretValue);
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
