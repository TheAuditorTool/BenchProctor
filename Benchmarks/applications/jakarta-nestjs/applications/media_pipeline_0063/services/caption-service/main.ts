import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { ExtractCaption } from "./caption_extract";
import { PublishReport } from "./publish_report";
import { EnrichLedger } from "./enrich_ledger";
import { FormatAsset } from "./format_asset";
import { BuildIndex } from "./build_index";
import { AuditReceipt } from "./audit_receipt";
import { AnnotateManifest } from "./annotate_manifest";
import { ValidateReceipt } from "./validate_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ExtractCaption, PublishReport, EnrichLedger, FormatAsset, BuildIndex, AuditReceipt, AnnotateManifest, ValidateReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
