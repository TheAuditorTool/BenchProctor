// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest81437 {

    @GET
    @Path("/BenchmarkTest81437")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest81437(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String data = String.format("%s", originValue);
        String accessLevel = "none";
        switch (data) {
            case "retry": accessLevel = "scoped-primary"; break;
            case "abort": accessLevel = "scoped-secondary+escalated"; break;
            case "ignore": accessLevel = "scoped-tertiary"; break;
            default: break;
        }
        response.setHeader("X-Access-Level", accessLevel);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
