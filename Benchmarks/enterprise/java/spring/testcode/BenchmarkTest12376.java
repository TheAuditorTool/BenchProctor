// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest12376 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest12376", consumes="multipart/form-data")
    public void BenchmarkTest12376(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = normalize(multipartValue);
        response.sendError(500, data);
    }
}
