// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest56371 {

    @PostMapping(path="/BenchmarkTest56371", consumes="multipart/form-data")
    public void BenchmarkTest56371(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        response.setHeader("X-Forwarded-For", uploadName);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
