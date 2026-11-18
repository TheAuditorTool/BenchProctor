// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

export const fetchThreshold = async (req: Request, res: Response): Promise<void> => {
  const headline = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const cohort = Buffer.from(headline, "base64").toString();
  const _coerced = parseInt(String(cohort), 10);
  const gauge = _coerced;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + gauge + "'");
  res.json({ accepted: true });
}
