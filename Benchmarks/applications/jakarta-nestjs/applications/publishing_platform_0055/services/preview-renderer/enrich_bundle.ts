// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("preview-renderer")
export class EnrichBundle {
  @Post("enrichBundle")
  async enrichBundle(@Req() req: Request): Promise<unknown> {
    const synopsis = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const byline: string = parts.join(',');
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + byline + "'");
    return { created: true };
  }
}
