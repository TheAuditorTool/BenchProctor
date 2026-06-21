// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;

@Path("/")
public class BenchmarkTest04646 {
    private static class UserInput {
        @jakarta.validation.constraints.NotNull
        public String payload;
        public UserInput() {}
        public UserInput(String payload) { this.payload = payload; }
    }

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest04646.class);
    private enum AllowedValue { INFO, WARN, ERROR, DEBUG }

    @POST
    @Path("/BenchmarkTest04646")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest04646(@Valid UserInput req, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String jsonValue = req.payload;
        String data;
        try { data = String.valueOf(Integer.parseInt(jsonValue)); }
        catch (NumberFormatException e) { data = jsonValue; }
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
