// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14796 {

    @GetMapping("/BenchmarkTest14796")
    public void BenchmarkTest14796(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String secretValue = "p4ssw0rd_test_xyz";
        String data;
        if (secretValue.length() > 256) { data = secretValue.substring(0, 256); }
        else { data = secretValue; }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
