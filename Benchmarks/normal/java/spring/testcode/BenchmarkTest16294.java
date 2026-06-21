// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest16294 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest16294.class);

    @GetMapping("/BenchmarkTest16294")
    public void BenchmarkTest16294(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        LOG.info("Action: {}", authHeader);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
