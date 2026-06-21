// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest43575 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest43575.class);

    @PostMapping("/BenchmarkTest43575")
    public void BenchmarkTest43575(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        if (!("true".equals(fieldValue) || "false".equals(fieldValue))) { response.sendError(400); return; }
        LOG.info("Action: {}", fieldValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
