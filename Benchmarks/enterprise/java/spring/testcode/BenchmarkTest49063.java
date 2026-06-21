// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest49063 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest49063.class);

    @PostMapping("/BenchmarkTest49063")
    public void BenchmarkTest49063(@RequestParam("field") String field, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String fieldValue = field != null ? field : "";
        String prefix = fieldValue.length() > 0 ? fieldValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = fieldValue.toLowerCase(); break;
            case "f": data = fieldValue.toUpperCase(); break;
            default: data = fieldValue.strip(); break;
        }
        LOG.info("request processed");
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
