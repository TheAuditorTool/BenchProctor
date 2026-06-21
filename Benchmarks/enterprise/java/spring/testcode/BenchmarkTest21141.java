// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest21141 {

    @PostMapping(path="/BenchmarkTest21141", consumes="multipart/form-data")
    public void BenchmarkTest21141(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        System.loadLibrary(multipartValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
