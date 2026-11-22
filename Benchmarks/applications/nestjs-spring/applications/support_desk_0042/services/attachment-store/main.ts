import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { StoreAttachment } from "./attachment_store";
import { BuildMacro } from "./build_macro";
import { RotateBundle } from "./rotate_bundle";
import { FetchTicket } from "./fetch_ticket";
import { ExportPolicy } from "./export_policy";
import { PublishManifest } from "./publish_manifest";
import { PublishHeader } from "./publish_header";
import { FormatHeader } from "./format_header";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, StoreAttachment, BuildMacro, RotateBundle, FetchTicket, ExportPolicy, PublishManifest, PublishHeader, FormatHeader],
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
