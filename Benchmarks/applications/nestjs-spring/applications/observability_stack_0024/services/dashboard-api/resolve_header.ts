// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import { DataSource } from "typeorm";

@Controller("dashboard-api")
export class ResolveHeader {
  @Post("resolveHeader")
  async resolveHeader(@Req() req: Request): Promise<unknown> {
    const summary = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const cohort: string = transform(summary);
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + cohort + "'");
    return { created: true };
  }
}
