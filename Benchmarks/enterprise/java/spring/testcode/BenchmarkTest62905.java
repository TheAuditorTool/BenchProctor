// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest62905 {

    @PostMapping(path="/BenchmarkTest62905", consumes="multipart/form-data")
    public void BenchmarkTest62905(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        request.getSession().setAttribute("data", String.valueOf(multipartValue));
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
