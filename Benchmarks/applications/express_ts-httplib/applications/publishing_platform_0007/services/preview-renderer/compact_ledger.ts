// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const compactLedger = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.body?.payload as string) || "";
  let byline;
  try { byline = JSON.parse(remark).value || ""; }
  catch (e) { byline = String(remark); }
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = :name", { name: byline }).getRawMany();
  res.json({ accepted: true });
}
