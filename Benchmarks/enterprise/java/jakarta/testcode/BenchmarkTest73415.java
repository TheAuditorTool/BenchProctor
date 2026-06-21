// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest73415 {

    @GET
    @Path("/BenchmarkTest73415")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest73415(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.text.MessageFormat fmt = new java.text.MessageFormat("payload={0}");
        String data = fmt.format(new Object[]{hostValue});
        request.isUserInRole("ADMIN");
        return Response.ok("{\"role\":\"admin\"}", MediaType.APPLICATION_JSON).build();
    }
}
