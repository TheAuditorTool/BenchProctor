// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03988 {

    private static String normalize(String v) { return v.strip(); }
    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest03988.class);

    @GetMapping("/BenchmarkTest03988")
    public void BenchmarkTest03988(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        String data = normalize(authHeader);
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
