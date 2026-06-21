// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest05105 {

    @POST
    @Path("/BenchmarkTest05105")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest05105(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        String routeResult = "unknown";
        switch (xmlValue) {
            case "retry": routeResult = "retry-handled"; break;
            case "abort": routeResult = "abort-handled"; break;
            default: routeResult = "fallback"; break;
        }
        response.setHeader("X-Route-Result", routeResult);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
