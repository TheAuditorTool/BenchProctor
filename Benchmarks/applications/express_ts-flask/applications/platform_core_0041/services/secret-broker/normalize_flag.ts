// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

export const normalizeFlag = async (req: Request, res: Response): Promise<void> => {
  const passage = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
  const tokens = String(passage).split(',').filter((t) => t.length > 0);
  const persona = tokens.join(' ');
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + persona + "'");
  res.json({ accepted: true });
}
