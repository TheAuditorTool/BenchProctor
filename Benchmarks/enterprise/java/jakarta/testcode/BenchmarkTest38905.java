// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest38905 {

    @GET
    @Path("/BenchmarkTest38905")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest38905(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        int boundedVal;
        try { boundedVal = Integer.parseInt(uaValue); }
        catch (NumberFormatException e) { return Response.status(400).build(); }
        if (boundedVal < 0 || boundedVal > 1048576) { return Response.status(400).build(); }
        long requested = boundedVal;
        long allocSize = requested + 1;
        response.setHeader("X-Alloc-Size", String.valueOf(allocSize));
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
