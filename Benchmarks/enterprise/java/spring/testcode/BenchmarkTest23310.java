// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23310 {

    @PostMapping(path="/BenchmarkTest23310", consumes="multipart/form-data")
    public void BenchmarkTest23310(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        new java.io.File(multipartValue).delete();
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
