import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { QuoteShipment } from "./shipment_quote";
import { ResolveLedger } from "./resolve_ledger";
import { BuildRoster } from "./build_roster";
import { CollectBatch } from "./collect_batch";
import { CompactShipment } from "./compact_shipment";
import { FormatPolicy } from "./format_policy";
import { ReconcileShipment } from "./reconcile_shipment";
import { AuditManifest } from "./audit_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, QuoteShipment, ResolveLedger, BuildRoster, CollectBatch, CompactShipment, FormatPolicy, ReconcileShipment, AuditManifest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
