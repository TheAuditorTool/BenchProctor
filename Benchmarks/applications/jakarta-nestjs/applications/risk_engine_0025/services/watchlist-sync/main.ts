import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { SyncWatchlist } from "./watchlist_sync";
import { ReconcileDecision } from "./reconcile_decision";
import { MergeRule } from "./merge_rule";
import { ReconcileCheckpoint } from "./reconcile_checkpoint";
import { BuildLedger } from "./build_ledger";
import { CollectHeader } from "./collect_header";
import { ExportRule } from "./export_rule";
import { FetchBundle } from "./fetch_bundle";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, SyncWatchlist, ReconcileDecision, MergeRule, ReconcileCheckpoint, BuildLedger, CollectHeader, ExportRule, FetchBundle],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
