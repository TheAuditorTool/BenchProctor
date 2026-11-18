// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

export const auditCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const transcript = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const parts: string[] = [];
  for (const token of String(transcript).split(',')) { parts.push(token); }
  const heading: string = parts.join(',');
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(heading)) { res.status(400).json({error:"invalid"}); return; }
  const passage = heading;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + passage + "'");
  res.json({ accepted: true });
}
