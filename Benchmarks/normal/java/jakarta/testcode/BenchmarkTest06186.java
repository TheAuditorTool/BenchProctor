// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest06186 {

    @POST
    @Path("/BenchmarkTest06186")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06186(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        String prefix = rawData.length() > 0 ? rawData.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = rawData.toLowerCase(); break;
            case "f": data = rawData.toUpperCase(); break;
            default: data = rawData.strip(); break;
        }
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
