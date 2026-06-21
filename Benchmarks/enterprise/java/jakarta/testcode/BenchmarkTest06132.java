// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest06132 {

    @GET
    @Path("/BenchmarkTest06132")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest06132(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        String prefix = originValue.length() > 0 ? originValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = originValue.toLowerCase(); break;
            case "f": data = originValue.toUpperCase(); break;
            default: data = originValue.strip(); break;
        }
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        System.setProperty("app.user.preference", data);
        response.setHeader("X-Config-Set", "app.user.preference");
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
