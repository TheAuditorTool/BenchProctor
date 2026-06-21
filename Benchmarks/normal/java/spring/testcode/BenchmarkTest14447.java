// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14447 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest14447.class);

    @GetMapping("/BenchmarkTest14447/{pathId}")
    public void BenchmarkTest14447(@PathVariable("pathId") String pathId, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        String prefix = pathValue.length() > 0 ? pathValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = pathValue.toLowerCase(); break;
            case "f": data = pathValue.toUpperCase(); break;
            default: data = pathValue.strip(); break;
        }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
