// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest29919 {

    @GET
    @Path("/BenchmarkTest29919/{pathId}")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest29919(@PathParam("pathId") String pathId, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String pathValue = pathId;
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(pathValue);
        String data = wrapper.toString();
        try {
            Integer.parseInt(data);
        } catch (NumberFormatException nfe) {
            return Response.status(400).entity("invalid number").build();
        }
        return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
    }
}
