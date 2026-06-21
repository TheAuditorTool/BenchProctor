// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00528 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest00528.class);

    @GetMapping("/BenchmarkTest00528")
    public void BenchmarkTest00528(HttpServletRequest request, HttpServletResponse response) throws Exception {
        String dotenvValue = java.util.Optional.ofNullable(System.getenv("DOTENV_VAR")).orElse("");
        java.util.function.Function<String, String> primary = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> stripChain = primary.andThen(String::strip);
        String data = stripChain.apply(dotenvValue);
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
