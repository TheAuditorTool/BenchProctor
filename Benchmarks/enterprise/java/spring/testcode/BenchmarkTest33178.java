// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest33178 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest33178.class);

    @GetMapping("/BenchmarkTest33178/{pathId}")
    public void BenchmarkTest33178(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.Map.Entry<String,String> kv = java.util.Map.entry(pathValue, "form");
        response.setHeader("X-Tuple-Context", kv.getValue());
        String data = kv.getKey();
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
