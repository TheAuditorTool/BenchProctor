// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest64347 {

    @PostMapping(path="/BenchmarkTest64347", consumes="multipart/form-data")
    public void BenchmarkTest64347(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        response.sendError(500, multipartValue);
    }
}
