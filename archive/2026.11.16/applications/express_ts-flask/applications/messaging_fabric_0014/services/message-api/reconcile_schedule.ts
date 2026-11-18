// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as fs from "fs";
import knex from "knex";

export const reconcileSchedule = async (req: Request, res: Response): Promise<void> => {
  const summary = fs.readFileSync("/tmp/data", "utf8");
  let bulletin;
  try { bulletin = JSON.parse(summary).value || ""; }
  catch (e) { bulletin = String(summary); }
  const _coerced = parseInt(String(bulletin), 10);
  const notice = _coerced;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + notice + "'");
  res.json({ accepted: true });
}
