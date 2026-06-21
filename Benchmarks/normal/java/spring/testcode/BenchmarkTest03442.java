// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest03442 {

    @PostMapping(path="/BenchmarkTest03442", consumes="multipart/form-data")
    public void BenchmarkTest03442(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        response.getWriter().print(multipartValue + ",data\n");
    }
}
