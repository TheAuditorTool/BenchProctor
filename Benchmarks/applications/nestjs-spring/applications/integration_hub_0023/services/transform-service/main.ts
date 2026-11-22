import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { TransformPayload } from "./payload_transform";
import { ReconcileLedger } from "./reconcile_ledger";
import { CompactConnector } from "./compact_connector";
import { ResolveCheckpoint } from "./resolve_checkpoint";
import { ArchivePolicy } from "./archive_policy";
import { ResolveDigest } from "./resolve_digest";
import { FormatRecord } from "./format_record";
import { ExportBatch } from "./export_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, TransformPayload, ReconcileLedger, CompactConnector, ResolveCheckpoint, ArchivePolicy, ResolveDigest, FormatRecord, ExportBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
