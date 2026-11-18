import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SubmitInvoice } from "./invoice_intake";
import { VerifyLedger } from "./verify_ledger";
import { RotateInvoice } from "./rotate_invoice";
import { ArchiveIndex } from "./archive_index";
import { ValidateSummary } from "./validate_summary";
import { LoadRoster } from "./load_roster";
import { ExportDunning } from "./export_dunning";
import { ExportBatch } from "./export_batch";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SubmitInvoice, VerifyLedger, RotateInvoice, ArchiveIndex, ValidateSummary, LoadRoster, ExportDunning, ExportBatch],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
