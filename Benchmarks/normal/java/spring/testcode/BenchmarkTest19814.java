// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest19814 {

    @PostMapping(path="/BenchmarkTest19814", consumes="multipart/form-data")
    public void BenchmarkTest19814(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        response.setContentType("text/html");
        response.getWriter().print(uploadName);
    }
}
