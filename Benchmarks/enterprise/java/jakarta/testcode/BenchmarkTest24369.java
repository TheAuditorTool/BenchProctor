// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import java.nio.file.Files;
import java.nio.file.Paths;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest24369 {

    private static String collapseWhitespace(String v) { return v.replaceAll("\\s+", " "); }

    @POST
    @Path("/BenchmarkTest24369")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest24369(@FormDataParam("file") java.io.InputStream fileStream, @FormDataParam("file") org.glassfish.jersey.media.multipart.FormDataContentDisposition fileDetail, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadName = fileDetail.getFileName();
        String data = collapseWhitespace(uploadName);
        java.util.concurrent.CompletableFuture.runAsync(() -> {
            try {
            Files.write(Paths.get("/var/uploads/" + data), "data".getBytes());
            } catch (Exception ex) { throw new RuntimeException(ex); }
        }).get();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
