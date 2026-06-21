// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.io.*;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest72590 {

    @POST
    @Path("/BenchmarkTest72590")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest72590(@FormDataParam("file") java.io.InputStream fileStream, @FormDataParam("file") org.glassfish.jersey.media.multipart.FormDataContentDisposition fileDetail, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadName = fileDetail.getFileName();
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + uploadName;
        String data = valueSupplier.get();
        java.security.MessageDigest md = java.security.MessageDigest.getInstance("SHA-256");
        byte[] hashed = md.digest(data.getBytes());
        try (java.io.FileWriter fw = new java.io.FileWriter("/var/data/secrets.txt")) {
            fw.write(java.util.Base64.getEncoder().encodeToString(hashed));
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
