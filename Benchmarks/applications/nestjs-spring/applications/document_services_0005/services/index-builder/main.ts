import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";

import { IndexDocument } from "./search_index";
import { AnnotateReport } from "./annotate_report";
import { BuildAttachment } from "./build_attachment";
import { CollectReport } from "./collect_report";
import { BuildCheckpoint } from "./build_checkpoint";
import { ExportWindow } from "./export_window";
import { PublishRoster } from "./publish_roster";
import { VerifyConfig } from "./verify_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, IndexDocument, AnnotateReport, BuildAttachment, CollectReport, BuildCheckpoint, ExportWindow, PublishRoster, VerifyConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
