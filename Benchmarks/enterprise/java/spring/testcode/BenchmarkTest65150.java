// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest65150 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest65150.class);

    @GetMapping("/BenchmarkTest65150")
    public void BenchmarkTest65150(@RequestParam("items") java.util.List<String> items, HttpServletRequest request, HttpServletResponse response) throws Exception {
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
