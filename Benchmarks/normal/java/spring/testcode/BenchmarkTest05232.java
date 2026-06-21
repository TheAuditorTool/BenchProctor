// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest05232 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest05232.class);

    @GetMapping("/BenchmarkTest05232")
    public void BenchmarkTest05232(@RequestParam("items") java.util.List<String> items, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        String prefix = queryArray.length() > 0 ? queryArray.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = queryArray.toLowerCase(); break;
            case "f": data = queryArray.toUpperCase(); break;
            default: data = queryArray.strip(); break;
        }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
