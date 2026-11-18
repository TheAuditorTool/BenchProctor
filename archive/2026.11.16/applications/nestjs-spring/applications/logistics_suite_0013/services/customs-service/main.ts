import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { DeclareCustoms } from "./customs_declare";
import { MergeShipment } from "./merge_shipment";
import { RenderProfile } from "./render_profile";
import { EnrichCheckpoint } from "./enrich_checkpoint";
import { ReconcileSnapshot } from "./reconcile_snapshot";
import { ExportSummary } from "./export_summary";
import { EnrichReport } from "./enrich_report";
import { LoadIndex } from "./load_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, DeclareCustoms, MergeShipment, RenderProfile, EnrichCheckpoint, ReconcileSnapshot, ExportSummary, EnrichReport, LoadIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
