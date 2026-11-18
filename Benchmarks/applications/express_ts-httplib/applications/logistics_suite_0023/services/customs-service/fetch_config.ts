// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const fetchConfig = async (req: Request, res: Response): Promise<void> => {
  const caption = (req.headers.referer as string) || "";
  const parts: string[] = [];
  for (const token of String(caption).split(',')) { parts.push(token); }
  const parcel: string = parts.join(',');
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + parcel + "'");
  res.json({ accepted: true });
}
