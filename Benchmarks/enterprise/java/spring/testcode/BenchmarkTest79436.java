// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79436 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest79436.class);

    @GetMapping("/BenchmarkTest79436")
    public void BenchmarkTest79436(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{refererValue});
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
