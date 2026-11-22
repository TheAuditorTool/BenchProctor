import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SearchKnowledge } from "./knowledge_search";
import { ReconcileBatch } from "./reconcile_batch";
import { NormalizeReport } from "./normalize_report";
import { MergeIndex } from "./merge_index";
import { MergeLedger } from "./merge_ledger";
import { ReconcileReceipt } from "./reconcile_receipt";
import { ExportConfig } from "./export_config";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SearchKnowledge, ReconcileBatch, NormalizeReport, MergeIndex, MergeLedger, ReconcileReceipt, ExportConfig],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
