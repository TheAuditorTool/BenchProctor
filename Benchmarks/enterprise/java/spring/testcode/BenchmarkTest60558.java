// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest60558 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest60558.class);

    @GetMapping("/BenchmarkTest60558")
    public void BenchmarkTest60558(@RequestHeader("Origin") String origin, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        java.util.function.Function<String,String> transform = v -> v.strip().replaceAll("\\s+", " ");
        String data = transform.apply(originValue);
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
