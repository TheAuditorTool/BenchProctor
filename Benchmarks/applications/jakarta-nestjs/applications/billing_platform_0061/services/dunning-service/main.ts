import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { SendDunningNotice } from "./dunning_notice";
import { EnrichSummary } from "./enrich_summary";
import { BuildInvoice } from "./build_invoice";
import { MergeStatement } from "./merge_statement";
import { RenderReceipt } from "./render_receipt";
import { RotateRecord } from "./rotate_record";
import { CollectLedger } from "./collect_ledger";
import { ValidateDunning } from "./validate_dunning";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SendDunningNotice, EnrichSummary, BuildInvoice, MergeStatement, RenderReceipt, RotateRecord, CollectLedger, ValidateDunning],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
