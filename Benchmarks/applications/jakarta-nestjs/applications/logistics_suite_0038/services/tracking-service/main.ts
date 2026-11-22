import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { PollTracking } from "./tracking_poll";
import { ValidateProfile } from "./validate_profile";
import { PruneLabel } from "./prune_label";
import { EnrichHeader } from "./enrich_header";
import { CompactShipment } from "./compact_shipment";
import { EnrichSummary } from "./enrich_summary";
import { ReconcileConfig } from "./reconcile_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PollTracking, ValidateProfile, PruneLabel, EnrichHeader, CompactShipment, EnrichSummary, ReconcileConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
