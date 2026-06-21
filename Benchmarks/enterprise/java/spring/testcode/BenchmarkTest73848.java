// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73848 {

    @PostMapping(path="/BenchmarkTest73848", consumes="multipart/form-data")
    public void BenchmarkTest73848(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = "[%s]".formatted(multipartValue);
        response.setContentType("text/html");
        response.getWriter().print(data);
    }
}
