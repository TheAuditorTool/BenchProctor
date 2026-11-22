// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("preview-renderer")
export class ValidateTaxonomy {
  @Post("validateTaxonomy")
  async validateTaxonomy(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const byline: string = transform(remark);
    const _coerced = parseInt(String(byline), 10);
    const addendum = _coerced;
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.query("SELECT * FROM users WHERE id = '" + addendum + "'");
    return { created: true };
  }
}
