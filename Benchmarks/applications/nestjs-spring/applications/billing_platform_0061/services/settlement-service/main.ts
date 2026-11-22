import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { RunSettlement } from "./settlement_batch";
import { EnrichManifest } from "./enrich_manifest";
import { LoadRecord } from "./load_record";
import { EnrichInvoice } from "./enrich_invoice";
import { NormalizeSummary } from "./normalize_summary";
import { RenderDunning } from "./render_dunning";
import { AuditProfile } from "./audit_profile";
import { EnrichRecord } from "./enrich_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunSettlement, EnrichManifest, LoadRecord, EnrichInvoice, NormalizeSummary, RenderDunning, AuditProfile, EnrichRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
