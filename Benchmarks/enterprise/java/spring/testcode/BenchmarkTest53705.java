// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest53705 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest53705.class);

    @GetMapping("/BenchmarkTest53705")
    public void BenchmarkTest53705(@RequestHeader("Authorization") String authorization, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String authHeader = authorization != null ? authorization : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replaceAll("[ ]+", " ");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::trim);
        String data = decorated.apply(authHeader);
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
