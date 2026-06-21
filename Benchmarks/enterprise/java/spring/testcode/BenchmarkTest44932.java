// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
public class BenchmarkTest44932 {

    @PostMapping(path="/BenchmarkTest44932", consumes="multipart/form-data")
    public void BenchmarkTest44932(@RequestPart("file") MultipartFile file, HttpServletRequest request, HttpServletResponse response) throws Exception {
        String uploadName = file != null ? file.getOriginalFilename() : "";
        String data;
        if (uploadName.length() > 256) { data = uploadName.substring(0, 256); }
        else { data = uploadName; }
        response.getWriter().print(data + ",data\n");
    }
}
