// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const rotateConversion = async (req: Request, res: Response): Promise<void> => {
  const snippet = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const addendum = snippet != null ? snippet : '';
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + addendum + "'").getRawMany();
  res.json({ accepted: true });
}
