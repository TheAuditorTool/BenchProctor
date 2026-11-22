// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const mergeCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const summary = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const consignment: string = transform(summary);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(consignment)) { res.status(400).json({error:"invalid"}); return; }
  const parcel = consignment;
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + parcel + "'").getRawMany();
  res.json({ accepted: true });
}
