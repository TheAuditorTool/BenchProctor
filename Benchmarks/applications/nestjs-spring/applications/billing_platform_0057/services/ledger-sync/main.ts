import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { PostLedgerEntry } from "./ledger_post";
import { MergeReport } from "./merge_report";
import { RotateLedger } from "./rotate_ledger";
import { PruneSummary } from "./prune_summary";
import { NormalizeInvoice } from "./normalize_invoice";
import { EnrichManifest } from "./enrich_manifest";
import { ValidateSummary } from "./validate_summary";
import { CollectHeader } from "./collect_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, PostLedgerEntry, MergeReport, RotateLedger, PruneSummary, NormalizeInvoice, EnrichManifest, ValidateSummary, CollectHeader],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
