// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest58159 {

    @POST
    @Path("/BenchmarkTest58159")
    @Consumes("text/plain")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest58159(String rawBody, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String rawData = rawBody != null ? rawBody : "";
        com.fasterxml.jackson.databind.JsonNode root = new com.fasterxml.jackson.databind.ObjectMapper().readTree(rawData);
        String data = root.path("value").asText();
        if (!("true".equals(data) || "false".equals(data))) { return Response.status(400).build(); }
        java.util.HashMap<String,Object> entity = new java.util.HashMap<>();
        String[] formPair = data.split("=", 2);
        if (formPair.length == 2) {
            entity.put(formPair[0], formPair[1]);
            response.setHeader("X-Field-Set", formPair[0]);
        }
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
