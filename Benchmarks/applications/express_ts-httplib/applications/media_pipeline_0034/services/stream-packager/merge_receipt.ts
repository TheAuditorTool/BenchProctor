// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { DataSource } from "typeorm";

export const mergeReceipt = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const rendition: string = normalize(synopsis);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(rendition)) { res.status(400).json({error:"invalid"}); return; }
  const montage = rendition;
  const _dataSource = ((globalThis as unknown as { _dataSource?: InstanceType<typeof DataSource> })._dataSource ??= new DataSource({ type: "postgres", url: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  if (!_dataSource.isInitialized) await _dataSource.initialize();
  await _dataSource.createQueryBuilder().select("u.id").from("users", "u").where("u.name = '" + montage + "'").getRawMany();
  res.json({ accepted: true });
}
