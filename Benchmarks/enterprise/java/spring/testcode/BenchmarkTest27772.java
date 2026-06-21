// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest27772 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest27772.class);

    @PostMapping(path="/BenchmarkTest27772", consumes="application/xml")
    public void BenchmarkTest27772(@RequestBody String xmlBody, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        LOG.info("Action: {}", xmlValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
