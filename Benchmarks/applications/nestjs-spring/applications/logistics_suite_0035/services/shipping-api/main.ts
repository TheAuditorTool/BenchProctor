import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QuoteShipment } from "./shipment_quote";
import { AuditWindow } from "./audit_window";
import { CollectSummary } from "./collect_summary";
import { ReconcileProfile } from "./reconcile_profile";
import { ExportProfile } from "./export_profile";
import { MergeLabel } from "./merge_label";
import { VerifyManifest } from "./verify_manifest";
import { VerifyWindow } from "./verify_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QuoteShipment, AuditWindow, CollectSummary, ReconcileProfile, ExportProfile, MergeLabel, VerifyManifest, VerifyWindow],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
