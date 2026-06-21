// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest20077 {

    @PostMapping(path="/BenchmarkTest20077", consumes="multipart/form-data")
    public void BenchmarkTest20077(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        response.setHeader("Access-Control-Allow-Origin", multipartValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
