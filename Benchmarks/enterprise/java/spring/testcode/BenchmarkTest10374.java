// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest10374 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest10374.class);

    @GetMapping("/BenchmarkTest10374")
    public void BenchmarkTest10374(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        LOG.info("Action: {}", userId);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
