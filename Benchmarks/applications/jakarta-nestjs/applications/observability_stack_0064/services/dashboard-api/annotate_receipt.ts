// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import { DataSource } from "typeorm";

@Controller("dashboard-api")
export class AnnotateReceipt {
  @Post("annotateReceipt")
  async annotateReceipt(@Req() req: Request): Promise<unknown> {
    const tagline = fs.readFileSync("/tmp/data", "utf8");
    const gauge = tagline != null ? tagline : '';
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = $1", [gauge]);
    return { created: true };
  }
}
