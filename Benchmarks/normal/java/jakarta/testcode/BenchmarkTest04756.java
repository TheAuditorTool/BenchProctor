// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04756 {

    private static String trimEnds(String v) { return v.trim(); }

    @GET
    @Path("/BenchmarkTest04756")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04756(@HeaderParam("Host") String host, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String hostValue = host != null ? host : "";
        String data = trimEnds(hostValue);
        String routeResult = "unknown";
        switch (data) {
            case "retry": routeResult = "retry-handled"; break;
            case "abort": routeResult = "abort-handled"; break;
            default: routeResult = "fallback"; break;
        }
        response.setHeader("X-Route-Result", routeResult);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
