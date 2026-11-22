// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
import { DataSource } from "typeorm";

export const mergeWindow = async (req: Request, res: Response): Promise<void> => {
  const summary = (await shared.mq.receive("app-events"));
  const transform = (v: string): string => v.trim();
  const phrase: string = transform(summary);
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + phrase + "'");
  res.json({ accepted: true });
}
