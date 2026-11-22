// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const mergeCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.body?.payload as string) || "";
  let consignment;
  try { consignment = JSON.parse(summary).value || ""; }
  catch (e) { consignment = String(summary); }
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = :name", { name: consignment }).getRawMany();
  res.json({ accepted: true });
}
