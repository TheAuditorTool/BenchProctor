// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest23209 {

    @PostMapping(path="/BenchmarkTest23209", consumes="multipart/form-data")
    public void BenchmarkTest23209(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        Integer.parseInt(multipartValue);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
