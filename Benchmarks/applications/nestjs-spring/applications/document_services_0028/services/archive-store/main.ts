import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { StoreArchive } from "./archive_store";
import { AnnotateRedaction } from "./annotate_redaction";
import { AnnotateReceipt } from "./annotate_receipt";
import { MergeConversion } from "./merge_conversion";
import { PublishManifest } from "./publish_manifest";
import { VerifyPolicy } from "./verify_policy";
import { VerifyConversion } from "./verify_conversion";
import { AuditBatch } from "./audit_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StoreArchive, AnnotateRedaction, AnnotateReceipt, MergeConversion, PublishManifest, VerifyPolicy, VerifyConversion, AuditBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
