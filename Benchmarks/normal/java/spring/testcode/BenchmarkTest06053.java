// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06053 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest06053.class);

    @GetMapping("/BenchmarkTest06053")
    public void BenchmarkTest06053(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        LOG.info("Action: {}", dotenvValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
