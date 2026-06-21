// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest43175 {

    @PostMapping(path="/BenchmarkTest43175", consumes="multipart/form-data")
    public void BenchmarkTest43175(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data;
        if (uploadName.length() > 256) { data = uploadName.substring(0, 256); }
        else { data = uploadName; }
        response.getWriter().print("<div>" + data + "</div>");
    }
}
