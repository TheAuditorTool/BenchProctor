package com.example.thumbnailservice;

public class JakartaBootstrap {

    @javax.ws.rs.Path("/health")
    public static class HealthResource {
        @javax.ws.rs.GET
        public javax.ws.rs.core.Response health() {
            return javax.ws.rs.core.Response.ok("ok").build();
        }
    }

    public static void main(String[] args) throws Exception {
        java.util.Map<String, String> initParams = new java.util.HashMap<>();
        initParams.put(
            "jersey.config.server.provider.classnames",
            "org.glassfish.jersey.server.filter.RolesAllowedDynamicFeature,org.glassfish.jersey.jackson.JacksonFeature,com.example.thumbnailservice.JakartaBootstrap$HealthResource,com.example.thumbnailservice.AnnotateSchedule,com.example.thumbnailservice.EnrichSnapshot,com.example.thumbnailservice.EnrichThreshold,com.example.thumbnailservice.NormalizeRecord,com.example.thumbnailservice.PruneManifest,com.example.thumbnailservice.PruneRecord,com.example.thumbnailservice.PublishConfig,com.example.thumbnailservice.RenderThumbnail");
        org.glassfish.grizzly.http.server.HttpServer server =
            org.glassfish.jersey.grizzly2.servlet.GrizzlyWebContainerFactory.create(
                java.net.URI.create("http://0.0.0.0:8080/"), initParams);
        server.start();
        Thread.currentThread().join();
    }
}
