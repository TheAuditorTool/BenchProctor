// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import { DataSource } from "typeorm";

export const fetchRoster = async (req: Request, res: Response): Promise<void> => {
  const citation = fs.readFileSync("/tmp/data", "utf8");
  let grievance;
  try { grievance = JSON.parse(citation).value || ""; }
  catch (e) { grievance = String(citation); }
  const _coerced = parseInt(String(grievance), 10);
  const inquiry = _coerced;
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + inquiry + "'");
  res.json({ accepted: true });
}
