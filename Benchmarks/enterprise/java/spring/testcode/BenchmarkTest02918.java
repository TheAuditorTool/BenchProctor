// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest02918 {

    @PostMapping(path="/BenchmarkTest02918", consumes="multipart/form-data")
    public void BenchmarkTest02918(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        if ("https://app.acmecdn.net".equals(uploadName)) response.setHeader("Access-Control-Allow-Origin", uploadName);
        response.setContentType("application/json");
        response.getWriter().print("{\"id\":0}");
    }
}
