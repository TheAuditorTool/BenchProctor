// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest18331 {

    @GET
    @Path("/BenchmarkTest18331")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18331(@HeaderParam("Referer") String referer, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String refererValue = referer != null ? referer : "";
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + refererValue + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
