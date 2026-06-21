// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02422 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest02422.class);

    @PostMapping(path="/BenchmarkTest02422", consumes="multipart/form-data")
    public void BenchmarkTest02422(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String prefix = multipartValue.length() > 0 ? multipartValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = multipartValue.toLowerCase(); break;
            case "f": data = multipartValue.toUpperCase(); break;
            default: data = multipartValue.strip(); break;
        }
        if (!("true".equals(data) || "false".equals(data))) { response.sendError(400); return; }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
