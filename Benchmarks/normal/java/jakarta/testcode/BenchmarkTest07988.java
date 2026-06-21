// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest07988 {

    @GET
    @Path("/BenchmarkTest07988")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest07988(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = String.join(" ", hostValue.split("\\s+"));
        new java.io.File(data).delete();
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
