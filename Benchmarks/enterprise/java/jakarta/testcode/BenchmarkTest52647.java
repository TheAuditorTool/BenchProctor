// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest52647 {

    @POST
    @Path("/BenchmarkTest52647")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest52647(@FormDataParam("file") java.io.InputStream fileStream, @FormDataParam("file") org.glassfish.jersey.media.multipart.FormDataContentDisposition fileDetail, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uploadName = fileDetail.getFileName();
        java.util.function.Supplier<String> valueSupplier = () -> "payload:" + uploadName;
        String data = valueSupplier.get();
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
