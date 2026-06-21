// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest73521 {

    private static String normalize(String v) { return v.strip(); }

    @PostMapping(path="/BenchmarkTest73521", consumes="multipart/form-data")
    public void BenchmarkTest73521(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = normalize(multipartValue);
        response.sendError(500, data);
    }
}
