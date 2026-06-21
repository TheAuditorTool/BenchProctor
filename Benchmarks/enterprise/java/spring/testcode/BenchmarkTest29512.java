// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest29512 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest29512.class);

    @GetMapping("/BenchmarkTest29512")
    public void BenchmarkTest29512(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String propValue = java.util.Optional.ofNullable(System.getProperty("app.value", "")).orElse("");
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(propValue, "http");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
