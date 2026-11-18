import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { TrackPresence } from "./presence_track";
import { ResolveReceipt } from "./resolve_receipt";
import { RotateDocument } from "./rotate_document";
import { BuildWindow } from "./build_window";
import { AnnotateReport } from "./annotate_report";
import { CompactWindow } from "./compact_window";
import { VerifyReceipt } from "./verify_receipt";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, TrackPresence, ResolveReceipt, RotateDocument, BuildWindow, AnnotateReport, CompactWindow, VerifyReceipt],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
