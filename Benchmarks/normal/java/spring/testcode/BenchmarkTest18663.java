// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest18663 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest18663.class);

    @GetMapping("/BenchmarkTest18663")
    public void BenchmarkTest18663(@RequestParam("items") java.util.List<String> items, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        String prefix = queryArray.length() > 0 ? queryArray.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = queryArray.toLowerCase(); break;
            case "f": data = queryArray.toUpperCase(); break;
            default: data = queryArray.strip(); break;
        }
        String processed = data.replace("\r", "").replace("\n", "").replaceAll("[A-Za-z0-9]{4,}", "****");
        LOG.info("Action: {}", processed);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
