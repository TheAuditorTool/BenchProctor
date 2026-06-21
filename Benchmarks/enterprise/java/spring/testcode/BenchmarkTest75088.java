// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest75088 {

    @PostMapping(path="/BenchmarkTest75088", consumes="multipart/form-data")
    public void BenchmarkTest75088(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = "" + multipartValue;
        response.getWriter().print("<div>" + data + "</div>");
    }
}
