// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest44203 {

    @GET
    @Path("/BenchmarkTest44203")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest44203(@HeaderParam("User-Agent") String userAgent, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String uaValue = userAgent != null ? userAgent : "";
        String data = uaValue.replace("\u0000", "");
        return Response.ok("{\"resource\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
