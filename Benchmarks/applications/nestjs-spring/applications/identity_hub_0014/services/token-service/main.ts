import { Controller, Get, Module } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";
import session from "express-session";

import { MintToken } from "./token_mint";
import { ExportIndex } from "./export_index";
import { EnrichManifest } from "./enrich_manifest";
import { ExportHeader } from "./export_header";
import { CompactLedger } from "./compact_ledger";
import { FetchManifest } from "./fetch_manifest";
import { MergeManifest } from "./merge_manifest";
import { FetchRoster } from "./fetch_roster";

@Controller("health")
class HealthController {
  @Get()
  check(): { status: string } {
    return { status: "ok" };
  }
}

@Module({
  controllers: [HealthController, MintToken, ExportIndex, EnrichManifest, ExportHeader, CompactLedger, FetchManifest, MergeManifest, FetchRoster],
})
class AppModule {}

async function bootstrap(): Promise<void> {
  const app = await NestFactory.create(AppModule);
  app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));
  await app.listen(3000, "0.0.0.0");
}

bootstrap();
