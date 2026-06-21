// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest76659 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest76659.class);

    @PostMapping("/BenchmarkTest76659")
    public void BenchmarkTest76659(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        LOG.info("Action: {}", fieldValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
