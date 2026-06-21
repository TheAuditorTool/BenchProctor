// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest55428 {

    @PostMapping(path="/BenchmarkTest55428", consumes="multipart/form-data")
    public void BenchmarkTest55428(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data = "" + uploadName;
        String normalized = java.text.Normalizer.normalize(data, java.text.Normalizer.Form.NFKC);
        response.setContentType("text/html");
        response.getWriter().print("<p>" + normalized + "</p>");
    }
}
