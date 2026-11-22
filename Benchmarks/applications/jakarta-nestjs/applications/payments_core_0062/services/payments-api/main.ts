import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { AuthorizePayment } from "./payment_authorize";
import { PublishDispute } from "./publish_dispute";
import { ArchiveDigest } from "./archive_digest";
import { AnnotateHeader } from "./annotate_header";
import { PublishSummary } from "./publish_summary";
import { BuildDigest } from "./build_digest";
import { FormatWindow } from "./format_window";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, AuthorizePayment, PublishDispute, ArchiveDigest, AnnotateHeader, PublishSummary, BuildDigest, FormatWindow],
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
