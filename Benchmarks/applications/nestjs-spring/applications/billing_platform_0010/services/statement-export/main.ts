import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";
import express from "express";
import multer from "multer";

import { BuildStatement } from "./statement_build";
import { ReconcileWindow } from "./reconcile_window";
import { SummarizeSummary } from "./summarize_summary";
import { ValidateCheckpoint } from "./validate_checkpoint";
import { ResolveHeader } from "./resolve_header";
import { ValidateSchedule } from "./validate_schedule";
import { ValidateWindow } from "./validate_window";
import { MergeSummary } from "./merge_summary";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, BuildStatement, ReconcileWindow, SummarizeSummary, ValidateCheckpoint, ResolveHeader, ValidateSchedule, ValidateWindow, MergeSummary],
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
