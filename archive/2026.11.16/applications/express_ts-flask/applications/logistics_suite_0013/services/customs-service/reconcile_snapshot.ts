// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { DataSource } from "typeorm";

export const reconcileSnapshot = async (req: Request, res: Response): Promise<void> => {
  const footnote = fs.readFileSync("/tmp/data", "utf8");
  let parcel;
  try { parcel = JSON.parse(footnote).value || ""; }
  catch (e) { parcel = String(footnote); }
  const _coerced = parseInt(String(parcel), 10);
  const consignment = _coerced;
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
