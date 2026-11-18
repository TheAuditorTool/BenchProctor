// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("dashboard-api")
export class EnrichPolicy {
  @Post("enrichPolicy")
  async enrichPolicy(@Req() req: Request): Promise<unknown> {
    const headline = (req.body as string) || "";
    let cohort;
    try { cohort = JSON.parse(headline).value || ""; }
    catch (e) { cohort = String(headline); }
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + cohort + "'");
    return { created: true };
  }
}
