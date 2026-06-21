// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest65359 {

    @GET
    @Path("/BenchmarkTest65359")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest65359(@HeaderParam("Origin") String origin, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String originValue = origin != null ? origin : "";
        if (!("true".equals(originValue) || "false".equals(originValue))) { return Response.status(400).build(); }
        response.setHeader("X-Forwarded-For", originValue);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
