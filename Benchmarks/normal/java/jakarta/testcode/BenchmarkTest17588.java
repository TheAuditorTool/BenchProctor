// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest17588 {

    @GET
    @Path("/BenchmarkTest17588")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest17588(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder envelope = new StringBuilder();
        envelope.append(uaValue);
        String data = envelope.toString();
        if (!data.isEmpty()) throw new Exception("processing error: " + data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
