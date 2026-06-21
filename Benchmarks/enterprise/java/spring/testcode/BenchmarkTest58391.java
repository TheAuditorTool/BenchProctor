// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.net.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest58391 {

    @PostMapping(path="/BenchmarkTest58391", consumes="multipart/form-data")
    public void BenchmarkTest58391(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.Map.Entry<String,String> tuple = java.util.Map.entry(multipartValue, "request");
        response.setHeader("X-Tuple-Context", tuple.getValue());
        String data = tuple.getKey();
        new Socket(data, 80).close();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
