// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest29997 {

    @PostMapping(path="/BenchmarkTest29997", consumes="multipart/form-data")
    public void BenchmarkTest29997(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = "[%s]".formatted(multipartValue);
        response.getWriter().print("{\"resource\":\"" + data + "\"}");
    }
}
