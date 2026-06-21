// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest09291 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @PostMapping(path="/BenchmarkTest09291", consumes="multipart/form-data")
    public void BenchmarkTest09291(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = collapseWhitespace(multipartValue);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        response.sendError(500, processed);
    }
}
