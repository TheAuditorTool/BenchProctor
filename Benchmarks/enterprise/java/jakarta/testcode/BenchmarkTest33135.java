// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest33135 {

    @GET
    @Path("/BenchmarkTest33135")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest33135(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String prefix = uaValue.length() > 0 ? uaValue.substring(0, 1).toLowerCase() : "";
        String data;
        switch (prefix) {
            case "h": data = uaValue.toLowerCase(); break;
            case "f": data = uaValue.toUpperCase(); break;
            default: data = uaValue.strip(); break;
        }
        Integer.parseInt(data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
