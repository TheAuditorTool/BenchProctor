// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest24600 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest24600.class);

    @PostMapping(path="/BenchmarkTest24600", consumes="text/plain")
    public void BenchmarkTest24600(@RequestBody String rawBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        LOG.info("Action: {}", rawData);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
