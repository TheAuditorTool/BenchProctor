// SPDX-License-Identifier: Apache-2.0
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.ws.rs.*;
import jakarta.ws.rs.core.Context;
import jakarta.ws.rs.core.MediaType;
import jakarta.ws.rs.core.Response;
import org.glassfish.jersey.media.multipart.FormDataParam;

@Path("/")
public class BenchmarkTest18014 {

    @POST
    @Path("/BenchmarkTest18014")
    @Consumes(MediaType.MULTIPART_FORM_DATA)
    @Produces(MediaType.APPLICATION_JSON)
    public Response BenchmarkTest18014(@FormDataParam("multipart_field") String multipartField, @Context HttpServletRequest request, @Context HttpServletResponse response) throws Exception {
        String multipartValue = multipartField != null ? multipartField : "";
        StringBuilder wrapper = new StringBuilder();
        wrapper.append(multipartValue);
        String data = wrapper.toString();
        String processed = data.length() > 64 ? data.substring(0, 64) : data;
        jakarta.el.ELProcessor elp = new jakarta.el.ELProcessor();
        Object rendered = elp.eval(processed);
        return Response.ok("<div>" + rendered + "</div>", MediaType.TEXT_HTML).build();
    }
}
