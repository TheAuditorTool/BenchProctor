import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { LookupSku } from "./sku_lookup";
import { ArchiveHeader } from "./archive_header";
import { EnrichHeader } from "./enrich_header";
import { LoadBatch } from "./load_batch";
import { RenderLedger } from "./render_ledger";
import { ResolveAllocation } from "./resolve_allocation";
import { RotateDigest } from "./rotate_digest";
import { ReconcileSummary } from "./reconcile_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, LookupSku, ArchiveHeader, EnrichHeader, LoadBatch, RenderLedger, ResolveAllocation, RotateDigest, ReconcileSummary],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
