import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import multer from "multer";

import { ValidateAddress } from "./address_validate";
import { SummarizeLabel } from "./summarize_label";
import { ValidateReport } from "./validate_report";
import { FormatBatch } from "./format_batch";
import { AuditCheckpoint } from "./audit_checkpoint";
import { AnnotateWindow } from "./annotate_window";
import { PublishRecord } from "./publish_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, ValidateAddress, SummarizeLabel, ValidateReport, FormatBatch, AuditCheckpoint, AnnotateWindow, PublishRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(multer().any());
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
