// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const publishSnapshot = async (req: Request, res: Response): Promise<void> => {
  const summary = process.env.DELIVERY_INPUT_0021 || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const phrase: string = normalize(summary);
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + phrase + "'").getRawMany();
  res.json({ accepted: true });
}
