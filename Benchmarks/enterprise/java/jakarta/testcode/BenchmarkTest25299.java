// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest25299 {

    @POST
    @Path("/BenchmarkTest25299")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest25299(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{rawData});
        new java.io.File(data).delete();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
