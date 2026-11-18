import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { UpdatePresence } from "./presence_update";
import { AnnotateReport } from "./annotate_report";
import { ExportBundle } from "./export_bundle";
import { FetchBundle } from "./fetch_bundle";
import { AuditBatch } from "./audit_batch";
import { EnrichRecord } from "./enrich_record";
import { NormalizeRecord } from "./normalize_record";
import { EnrichDelivery } from "./enrich_delivery";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, UpdatePresence, AnnotateReport, ExportBundle, FetchBundle, AuditBatch, EnrichRecord, NormalizeRecord, EnrichDelivery],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
