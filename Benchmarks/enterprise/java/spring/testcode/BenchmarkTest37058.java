// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest37058 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest37058.class);

    @GetMapping("/BenchmarkTest37058")
    public void BenchmarkTest37058(@RequestParam("items") java.util.List<String> items, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String queryArray = items.get(0) != null ? items.get(0) : "";
        java.util.List<String> tokens = new java.util.ArrayList<>();
        for (String token : queryArray.split(",")) { tokens.add(token.trim()); }
        String data = String.join(",", tokens);
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
