// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest27667 {

    @POST
    @Path("/BenchmarkTest27667")
    @Consumes(MediaType.APPLICATION_XML)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest27667(String xmlBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String xmlValue = xmlBody;
        java.util.Map.Entry<String,String> entry = java.util.Map.entry(xmlValue, "query");
        response.setHeader("X-Tuple-Context", entry.getValue());
        String data = entry.getKey();
        if ("admin".equals(data) || "ROLE_ADMIN".equals(data)) {
            return Response.ok("{\"status\":\"ok\"}", MediaType.APPLICATION_JSON).build();
        }
        return Response.status(403).entity("forbidden").build();
    }
}
