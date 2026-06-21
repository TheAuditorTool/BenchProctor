// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest14379 {

    @PostMapping(path="/BenchmarkTest14379", consumes="multipart/form-data")
    public void BenchmarkTest14379(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = java.net.URLDecoder.decode(multipartValue, "UTF-8");
        response.getWriter().print("<div>" + data + "</div>");
    }
}
