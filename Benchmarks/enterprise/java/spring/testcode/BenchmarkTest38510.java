// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest38510 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest38510.class);

    @GetMapping("/BenchmarkTest38510")
    public void BenchmarkTest38510(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        String prefix = propValue.length() > 0 ? propValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = propValue.toLowerCase(); break;
            case "f": data = propValue.toUpperCase(); break;
            default: data = propValue.strip(); break;
        }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
