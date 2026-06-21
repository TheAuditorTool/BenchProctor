// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest39401 {

    @GET
    @Path("/BenchmarkTest39401/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest39401(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        StringBuilder payload = new StringBuilder();
        payload.append(pathValue);
        String data = payload.toString();
        response.setContentType("application/json");
        return Response.ok("{\"echo\":\"" + data + "\"}", MediaType.APPLICATION_JSON).build();
    }
}
