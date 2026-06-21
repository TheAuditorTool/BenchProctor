// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03901 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest03901.class);

    @PostMapping(path="/BenchmarkTest03901", consumes="multipart/form-data")
    public void BenchmarkTest03901(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data;
        if (multipartValue.length() > 256) { data = multipartValue.substring(0, 256); }
        else { data = multipartValue; }
        if (!data.matches("^[a-zA-Z0-9_.-]+$")) { response.sendError(400); return; }
        LOG.info("Action: {}", data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
