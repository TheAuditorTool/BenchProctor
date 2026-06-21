// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest21019 {

    @GET
    @Path("/BenchmarkTest21019/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest21019(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(pathValue);
        String data = wrapper.toString();
        response.setHeader("X-Forwarded-For", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
