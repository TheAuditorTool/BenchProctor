// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest37112 {

    @PostMapping(path="/BenchmarkTest37112", consumes="multipart/form-data")
    public void BenchmarkTest37112(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        response.getWriter().print("<input type=\"text\" name=\"q\" value=\"" + uploadName + "\">");
    }
}
