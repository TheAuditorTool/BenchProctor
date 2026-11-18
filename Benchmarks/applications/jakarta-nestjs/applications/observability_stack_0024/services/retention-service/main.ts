import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SweepRetention } from "./retention_sweep";
import { LoadWindow } from "./load_window";
import { ReconcileReport } from "./reconcile_report";
import { EnrichWindow } from "./enrich_window";
import { RotateDigest } from "./rotate_digest";
import { ExportSummary } from "./export_summary";
import { AuditBundle } from "./audit_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SweepRetention, LoadWindow, ReconcileReport, EnrichWindow, RotateDigest, ExportSummary, AuditBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
