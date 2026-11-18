// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const formatCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const passage = (req.body.payload as string) || "";
  const parts: string[] = [];
  for (const token of String(passage).split(',')) { parts.push(token); }
  const montage: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(montage)) { res.status(400).json({error:"invalid"}); return; }
  const rendition = montage;
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + rendition + "'");
  res.json({ accepted: true });
}
