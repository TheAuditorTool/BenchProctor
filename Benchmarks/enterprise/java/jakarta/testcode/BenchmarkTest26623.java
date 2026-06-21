// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest26623 {

    private static String stripWhitespace(String v) { return v.strip(); }

    @POST
    @Path("/BenchmarkTest26623")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest26623(@FormDataParam("file") java.io.InputStream fileStream, @FormDataParam("file") org.glassfish.jersey.media.multipart.FormDataContentDisposition fileDetail, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadName = fileDetail.getFileName();
        String data = stripWhitespace(uploadName);
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        int requested = Integer.parseInt(processed);
        int allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
