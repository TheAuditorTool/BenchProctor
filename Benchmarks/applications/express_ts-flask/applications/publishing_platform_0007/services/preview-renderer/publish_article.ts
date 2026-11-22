// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import { DataSource } from "typeorm";

export const publishArticle = async (req: Request, res: Response): Promise<void> => {
  const remark = (req.query.id as string) || "";
  const transform = (v: string): string => v.trim();
  const byline: string = transform(remark);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(byline)) { res.status(400).json({error:"invalid"}); return; }
  const addendum = byline;
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + addendum + "'").getRawMany();
  res.json({ accepted: true });
}
