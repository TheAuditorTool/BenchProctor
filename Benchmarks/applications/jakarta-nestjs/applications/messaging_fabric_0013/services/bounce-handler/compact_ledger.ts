// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { DataSource } from "typeorm";

@Controller("bounce-handler")
export class CompactLedger {
  @Post("compactLedger")
  async compactLedger(@Req() req: Request): Promise<unknown> {
    const summary = JSON.parse(fs.readFileSync("/etc/app/config.json", "utf8")).value;
    let bulletin;
    try { bulletin = JSON.parse(summary).value || ""; }
    catch (e) { bulletin = String(summary); }
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + bulletin + "'");
    return { created: true };
  }
}
