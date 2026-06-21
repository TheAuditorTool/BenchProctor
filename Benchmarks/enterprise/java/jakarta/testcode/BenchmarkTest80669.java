// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest80669 {

    @GET
    @Path("/BenchmarkTest80669")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest80669(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        return Response.ok(String.valueOf(originValue), MediaType.TEXT_HTML).build();
    }
}
