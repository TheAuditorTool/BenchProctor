// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest79539 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest79539.class);

    @GetMapping("/BenchmarkTest79539")
    public void BenchmarkTest79539(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(originValue)); }
        catch (NumberFormatException e) { data = originValue; }
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
