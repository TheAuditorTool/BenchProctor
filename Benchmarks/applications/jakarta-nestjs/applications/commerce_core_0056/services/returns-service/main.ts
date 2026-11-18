import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { RequestReturn } from "./return_request";
import { CompactWindow } from "./compact_window";
import { ArchiveLedger } from "./archive_ledger";
import { ExportWindow } from "./export_window";
import { CollectLedger } from "./collect_ledger";
import { RotateWindow } from "./rotate_window";
import { CompactRecord } from "./compact_record";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, RequestReturn, CompactWindow, ArchiveLedger, ExportWindow, CollectLedger, RotateWindow, CompactRecord],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
