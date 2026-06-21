// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest48660 {

    @GET
    @Path("/BenchmarkTest48660")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest48660(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = "[%s]".formatted(hostValue);
        int divisor = Integer.parseInt(data);
        if (divisor == 0) { return Response.status(400).build(); }
        int result = 100 / divisor;
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
