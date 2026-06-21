// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest17061 {

    private static final org.slf4j.Logger LOG = org.slf4j.LoggerFactory.getLogger(BenchmarkTest17061.class);
    private enum AllowedValue { INFO, WARN, ERROR, DEBUG }

    @POST
    @Path("/BenchmarkTest17061")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest17061(@FormDataParam("multipart_field") String multipartField, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        String data = "[%s]".formatted(multipartValue);
        try { AllowedValue.valueOf(data.toUpperCase().replace("-", "_")); }
        catch (IllegalArgumentException e) { data = AllowedValue.values()[0].name().toLowerCase(); }
        LOG.info("Action: {}", data);
        return Response.ok("{\"ready\":true}", MediaType.APPLICATION_JSON).build();
    }
}
