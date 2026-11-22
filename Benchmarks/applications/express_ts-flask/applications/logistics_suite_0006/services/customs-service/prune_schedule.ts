// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const pruneSchedule = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(summary);
  const consignment: string = readInput();
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.query("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
