import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { RenderPreview } from "./preview_render";
import { RenderLedger } from "./render_ledger";
import { LoadConfig } from "./load_config";
import { ArchiveRecord } from "./archive_record";
import { BuildLedger } from "./build_ledger";
import { PublishArticle } from "./publish_article";
import { ValidateTaxonomy } from "./validate_taxonomy";
import { BuildWindow } from "./build_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RenderPreview, RenderLedger, LoadConfig, ArchiveRecord, BuildLedger, PublishArticle, ValidateTaxonomy, BuildWindow],
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
