// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest00944 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest00944.class);

    @GetMapping("/BenchmarkTest00944")
    public void BenchmarkTest00944(@RequestHeader("Referer") String referer, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        java.util.function.Function<String, String> initialFn = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> normalized = initialFn.andThen(String::strip);
        String data = normalized.apply(refererValue);
        LOG.info("audit actor={} action=revoke_sessions target={}", request.getSession().getAttribute("user"), data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
