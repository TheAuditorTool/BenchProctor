// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest59903 {

    @GetMapping("/BenchmarkTest59903")
    public void BenchmarkTest59903(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        String prefix = dotenvValue.length() > 0 ? dotenvValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = dotenvValue.toLowerCase(); break;
            case "f": data = dotenvValue.toUpperCase(); break;
            default: data = dotenvValue.strip(); break;
        }
        try (java.sql.Connection authConn = java.sql.DriverManager.getConnection(
                "jdbc:postgresql://db.svc.local/app", "appuser", data)) {
            response.getWriter().print("{\"auth\":\"ok\"}");
        }
    }
}
