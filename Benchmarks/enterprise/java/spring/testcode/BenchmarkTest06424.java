// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest06424 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest06424.class);

    @GetMapping("/BenchmarkTest06424/{pathId}")
    public void BenchmarkTest06424(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        java.util.function.Function<String, String> initialFn = s -> s.replace("\t", " ");
        java.util.function.Function<String, String> transformed = initialFn.andThen(String::strip);
        String data = transformed.apply(pathValue);
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
