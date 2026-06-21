// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43971 {

    private static String normalize(String v) { return v.strip(); }
    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest43971.class);

    @GetMapping("/BenchmarkTest43971")
    public void BenchmarkTest43971(@RequestParam("id") String id, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = normalize(userId);
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
