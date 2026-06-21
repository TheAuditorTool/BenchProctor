// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest34189 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest34189.class);

    @GetMapping("/BenchmarkTest34189")
    public void BenchmarkTest34189(@RequestHeader("User-Agent") String userAgent, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String prefix = uaValue.length() > 0 ? uaValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = uaValue.toLowerCase(); break;
            case "f": data = uaValue.toUpperCase(); break;
            default: data = uaValue.strip(); break;
        }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
