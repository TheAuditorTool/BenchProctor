// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest77877 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest77877.class);

    @GetMapping("/BenchmarkTest77877")
    public void BenchmarkTest77877(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        LOG.info("Action: {}", refererValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
