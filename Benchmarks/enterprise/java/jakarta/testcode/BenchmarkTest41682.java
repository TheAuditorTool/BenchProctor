// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest41682 {

    @GET
    @Path("/BenchmarkTest41682")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest41682(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data;
        if (uaValue.length() > 256) { data = uaValue.substring(0, 256); }
        else { data = uaValue; }
        try {
            Integer.parseInt(data);
        } catch (Exception e) { }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
