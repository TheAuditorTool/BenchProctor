// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;

@RestController
public class BenchmarkTest02253 {

    @PostMapping(path="/BenchmarkTest02253", consumes="multipart/form-data")
    public void BenchmarkTest02253(@RequestPart("multipart_field") String multipartField, HttpServletRequest request, HttpServletResponse response) throws Exception {
        response.sendError(500, "Internal error");
    }
}
