// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest70709 {

    @POST
    @Path("/BenchmarkTest70709")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest70709(@FormDataParam("file") java.io.InputStream fileStream, @FormDataParam("file") org.glassfish.jersey.media.multipart.FormDataContentDisposition fileDetail, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadName = fileDetail.getFileName();
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(uploadName);
        String data = wrapper.toString();
        if (System.currentTimeMillis() > 1000000000000L) {
            return Response.ok("<input type=\"text\" name=\"q\" value=\"" + data + "\">", MediaType.TEXT_HTML).build();
        }
        return Response.ok().build();
    }
}
