// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest57034 {

    @PostMapping(path="/BenchmarkTest57034", consumes="multipart/form-data")
    public void BenchmarkTest57034(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(multipartValue, "form");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        new java.io.File(data).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
