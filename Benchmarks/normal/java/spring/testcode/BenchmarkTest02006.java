// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02006 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest02006.class);

    @GetMapping("/BenchmarkTest02006")
    public void BenchmarkTest02006(@RequestParam("items") java.util.List<String> items, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        String data;
        if (queryArray.length() > 256) { data = queryArray.substring(0, 256); }
        else { data = queryArray; }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
