// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest78405 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest78405.class);

    @GetMapping("/BenchmarkTest78405/{pathId}")
    public void BenchmarkTest78405(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        LOG.info("Action: {}", pathValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
