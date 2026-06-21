// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest64972 {

    private static final java.util.concurrent.atomic.AtomicReference<String> atomicValue = new java.util.concurrent.atomic.AtomicReference<>();

    @GET
    @Path("/BenchmarkTest64972")
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest64972(@QueryParam("id") String id, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String userId = id != null ? id : "";
        atomicValue.set(userId);
        String data = atomicValue.get();
        if (!data.matches("^[\\w\\s./\\\\:<>=_'\\\"!()\\[\\]{}$-]+$")) {
            return Response.status(400).entity("forbidden").build();
        }
        com.fasterxml.jackson.databind.ObjectMapper unsafeMapper = new com.fasterxml.jackson.databind.ObjectMapper();
        unsafeMapper.activateDefaultTyping(com.fasterxml.jackson.databind.jsontype.BasicPolymorphicTypeValidator.builder().allowIfBaseType(Object.class).build(), com.fasterxml.jackson.databind.ObjectMapper.DefaultTyping.NON_FINAL);
        Object polymorphicObj = unsafeMapper.readValue(data, Object.class);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
