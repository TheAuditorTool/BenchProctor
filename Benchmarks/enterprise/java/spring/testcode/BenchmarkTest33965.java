// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest33965 {

    @GetMapping("/BenchmarkTest33965")
    public void BenchmarkTest33965(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        StringBuilder carrier = new StringBuilder();
        carrier.append(userId);
        String data = carrier.toString();
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
