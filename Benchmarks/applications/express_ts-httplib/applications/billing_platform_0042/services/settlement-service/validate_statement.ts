// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import knex from "knex";

export const validateStatement = async (req: Request, res: Response): Promise<void> => {
  const remark = fs.readFileSync("/tmp/data", "utf8");
  const transform = (v: string): string => v.trim();
  const remittance: string = transform(remark);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(remittance)) { res.status(400).json({error:"invalid"}); return; }
  const dunning = remittance;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + dunning + "'");
  res.json({ accepted: true });
}
