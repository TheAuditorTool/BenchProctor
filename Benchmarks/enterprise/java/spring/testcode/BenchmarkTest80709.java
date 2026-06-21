// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest80709 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest80709.class);

    @GetMapping("/BenchmarkTest80709")
    public void BenchmarkTest80709(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String configValue = java.util.Optional.ofNullable(new String(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get("/etc/app/config.json")))).orElse("");
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(configValue, "cookie");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
