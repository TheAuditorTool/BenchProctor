// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest20458 {

    @GET
    @Path("/BenchmarkTest20458")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest20458(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data;
        try { data = String.valueOf(Integer.parseInt(uaValue)); }
        catch (NumberFormatException e) { data = uaValue; }
        try {
            Integer.parseInt(data);
        } catch (Exception e) { }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
