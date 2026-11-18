// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { DataSource } from "typeorm";

export const formatCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const passage = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const montage = Buffer.from(passage, "base64").toString();
  const _coerced = parseInt(String(montage), 10);
  const rendition = _coerced;
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + rendition + "'");
  res.json({ accepted: true });
}
