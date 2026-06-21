// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest67819 {

    @PostMapping(path="/BenchmarkTest67819", consumes="multipart/form-data")
    public void BenchmarkTest67819(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        java.util.Map.Entry<String,String> edge = java.util.Map.entry(multipartValue, "query");
        response.setHeader("X-Tuple-Context", edge.getValue());
        String data = edge.getKey();
        request.setAttribute("hidden_form_field", data);
        request.getRequestDispatcher("/dashboard").forward(request, response);
    }
}
