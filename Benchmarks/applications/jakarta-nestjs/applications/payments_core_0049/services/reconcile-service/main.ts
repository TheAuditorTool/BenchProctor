import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { RunReconciliation } from "./reconcile_batch";
import { ExportPayout } from "./export_payout";
import { NormalizeIndex } from "./normalize_index";
import { EnrichHeader } from "./enrich_header";
import { EnrichConfig } from "./enrich_config";
import { ReconcileDigest } from "./reconcile_digest";
import { ResolveConfig } from "./resolve_config";
import { AnnotateIndex } from "./annotate_index";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RunReconciliation, ExportPayout, NormalizeIndex, EnrichHeader, EnrichConfig, ReconcileDigest, ResolveConfig, AnnotateIndex],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
