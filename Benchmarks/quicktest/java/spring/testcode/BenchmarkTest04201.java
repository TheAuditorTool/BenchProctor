// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest04201 {

    @PostMapping(path="/BenchmarkTest04201", consumes="multipart/form-data")
    public void BenchmarkTest04201(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        if (!request.isUserInRole("ADMIN")) {
            response.sendError(403, "forbidden"); return;
        }
        response.getWriter().print("{\"role\":\"admin\"}");
    }
}
