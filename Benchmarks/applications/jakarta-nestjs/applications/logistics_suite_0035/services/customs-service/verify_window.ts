// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("customs-service")
export class VerifyWindow {
  @Post("verifyWindow")
  async verifyWindow(@Req() req: Request): Promise<unknown> {
    const phrase = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const parcel = phrase != null ? phrase : '';
    const _coerced = parseInt(String(parcel), 10);
    const consignment = _coerced;
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + consignment + "'");
    return { created: true };
  }
}
