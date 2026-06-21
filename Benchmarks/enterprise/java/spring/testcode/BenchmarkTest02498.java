// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest02498 {

    @PostMapping(path="/BenchmarkTest02498", consumes="multipart/form-data")
    public void BenchmarkTest02498(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String processed = org.owasp.encoder.Encode.forHtml(uploadName);
        response.getWriter().print("<div>" + processed + "</div>");
    }
}
