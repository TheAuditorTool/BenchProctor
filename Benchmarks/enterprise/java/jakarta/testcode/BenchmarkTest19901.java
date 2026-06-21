// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest19901 {

    @GET
    @Path("/BenchmarkTest19901")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest19901(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        StringBuilder payload = new StringBuilder();
        payload.append(uaValue);
        String data = payload.toString();
        String accessLevel = "none";
        switch (data) {
            case "retry": accessLevel = "scoped-primary";
            case "abort": accessLevel = accessLevel + "+escalated"; break;
            case "ignore": accessLevel = "scoped-tertiary"; break;
            default: break;
        }
        response.setHeader("X-Access-Level", accessLevel);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
