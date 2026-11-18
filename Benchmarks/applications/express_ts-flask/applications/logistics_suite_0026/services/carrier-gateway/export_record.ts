// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

export const exportRecord = async (req: Request, res: Response): Promise<void> => {
  const citation = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parcel = Buffer.from(citation, "base64").toString();
  const _coerced = parseInt(String(parcel), 10);
  const consignment = _coerced;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + consignment + "'");
  res.json({ accepted: true });
}
