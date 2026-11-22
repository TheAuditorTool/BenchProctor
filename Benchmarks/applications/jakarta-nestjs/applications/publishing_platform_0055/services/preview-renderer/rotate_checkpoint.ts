// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { DataSource } from "typeorm";

@Controller("preview-renderer")
export class RotateCheckpoint {
  @Post("rotateCheckpoint")
  async rotateCheckpoint(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body as string) || "";
    const byline = Buffer.from(synopsis, "utf-8").toString();
    const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
    if (!_dataSource.isInitialized) await _dataSource.initialize();
    await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = :name", { name: byline }).getRawMany();
    return { created: true };
  }
}
