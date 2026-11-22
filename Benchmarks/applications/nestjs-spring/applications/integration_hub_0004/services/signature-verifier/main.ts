import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { VerifySignature } from "./signature_verify";
import { ReconcileSummary } from "./reconcile_summary";
import { SummarizeLedger } from "./summarize_ledger";
import { RotateLedger } from "./rotate_ledger";
import { ValidateBatch } from "./validate_batch";
import { FetchPolicy } from "./fetch_policy";
import { EnrichReport } from "./enrich_report";
import { RenderManifest } from "./render_manifest";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, VerifySignature, ReconcileSummary, SummarizeLedger, RotateLedger, ValidateBatch, FetchPolicy, EnrichReport, RenderManifest],
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
