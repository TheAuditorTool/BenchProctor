// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";
import { createClient } from "redis";

export const reconcileCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const heading = (await _cache.get("user_data")) || "";
  const consignment = heading != null ? heading : '';
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
