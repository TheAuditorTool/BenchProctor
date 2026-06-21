// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest13523 {

    @PostMapping(path="/BenchmarkTest13523", consumes="multipart/form-data")
    public void BenchmarkTest13523(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = String.format("payload=%s", multipartValue);
        response.sendRedirect(data);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
