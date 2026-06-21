// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest48701 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest48701.class);

    @GetMapping("/BenchmarkTest48701/{pathId}")
    public void BenchmarkTest48701(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        LOG.info("Action: {}", pathValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
