// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest61417 {

    @GET
    @Path("/BenchmarkTest61417")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest61417(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        java.io.StringWriter sw = new java.io.StringWriter();
        new java.io.PrintWriter(sw).printf("%s", hostValue);
        String data = sw.toString();
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException e) {
            response.sendError(400, e.getMessage()); return Response.ok().build();
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
