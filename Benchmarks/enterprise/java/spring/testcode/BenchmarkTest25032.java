// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest25032 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest25032.class);

    @GetMapping("/BenchmarkTest25032")
    public void BenchmarkTest25032(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        String prefix = dotenvValue.length() > 0 ? dotenvValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = dotenvValue.toLowerCase(); break;
            case "f": data = dotenvValue.toUpperCase(); break;
            default: data = dotenvValue.strip(); break;
        }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
