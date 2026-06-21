// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00510 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest00510.class);

    @GetMapping("/BenchmarkTest00510")
    public void BenchmarkTest00510(@CookieValue("session_token") String sessionToken, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String cookieValue = sessionToken != null ? sessionToken : "";
        java.util.function.Function<String, String> tabNormalizer = s -> s.replace("\r", "").replace("\n", "");
        java.util.function.Function<String, String> decorated = tabNormalizer.andThen(String::strip);
        String data = decorated.apply(cookieValue);
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
