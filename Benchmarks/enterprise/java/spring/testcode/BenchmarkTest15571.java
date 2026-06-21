// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest15571 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest15571.class);

    @PostMapping(path="/BenchmarkTest15571", consumes="text/plain")
    public void BenchmarkTest15571(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        LOG.info("Action: {}", rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
