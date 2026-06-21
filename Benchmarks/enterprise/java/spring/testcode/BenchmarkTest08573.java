// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest08573 {

    @PostMapping(path="/BenchmarkTest08573", consumes="multipart/form-data")
    public void BenchmarkTest08573(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data = String.format("payload=%s", uploadName);
        response.getWriter().print("<div>" + data + "</div>");
    }
}
