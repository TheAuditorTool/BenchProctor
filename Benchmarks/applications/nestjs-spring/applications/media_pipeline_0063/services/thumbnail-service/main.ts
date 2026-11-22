import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { RenderThumbnail } from "./thumbnail_render";
import { PruneManifest } from "./prune_manifest";
import { EnrichThreshold } from "./enrich_threshold";
import { EnrichLedger } from "./enrich_ledger";
import { FormatAsset } from "./format_asset";
import { BuildIndex } from "./build_index";
import { AuditReceipt } from "./audit_receipt";
import { AnnotateManifest } from "./annotate_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RenderThumbnail, PruneManifest, EnrichThreshold, EnrichLedger, FormatAsset, BuildIndex, AuditReceipt, AnnotateManifest],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
