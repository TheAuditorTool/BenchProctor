import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { ValidateAddress } from "./address_validate";
import { SummarizeShipment } from "./summarize_shipment";
import { EnrichIndex } from "./enrich_index";
import { ValidateDigest } from "./validate_digest";
import { ExportSummary } from "./export_summary";
import { FetchDigest } from "./fetch_digest";
import { ExportReceipt } from "./export_receipt";
import { PruneCheckpoint } from "./prune_checkpoint";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ValidateAddress, SummarizeShipment, EnrichIndex, ValidateDigest, ExportSummary, FetchDigest, ExportReceipt, PruneCheckpoint],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
