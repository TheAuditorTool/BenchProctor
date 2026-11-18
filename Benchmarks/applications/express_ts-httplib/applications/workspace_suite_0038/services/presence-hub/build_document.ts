// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { DataSource } from "typeorm";

export const buildDocument = async (req: Request, res: Response): Promise<void> => {
  const preface = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const parts: string[] = [];
  for (const token of String(preface).split(',')) { parts.push(token); }
  const remark: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(remark)) { res.status(400).json({error:"invalid"}); return; }
  const wording = remark;
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + wording + "'");
  res.json({ accepted: true });
}
