// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest68278 {

    @GET
    @Path("/BenchmarkTest68278")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest68278(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        String data = java.net.URLDecoder.decode(userId, "UTF-8");
        com.fasterxml.jackson.databind.ObjectMapper unsafeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        unsafeMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
        Object polymorphicObj = unsafeMapper.readValue(data, Object.class);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
