// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75587 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest75587.class);

    @GetMapping("/BenchmarkTest75587")
    public void BenchmarkTest75587(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        LOG.info("Action: {}", dotenvValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
