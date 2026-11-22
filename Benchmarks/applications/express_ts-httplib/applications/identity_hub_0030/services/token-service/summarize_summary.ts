// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

export const summarizeSummary = async (req: Request, res: Response): Promise<void> => {
  const tagline = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
  const parts: string[] = [];
  for (const token of String(tagline).split(',')) { parts.push(token); }
  const persona: string = parts.join(',');
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.select("id", "name").from("users").whereRaw("name = '" + persona + "'");
  res.json({ accepted: true });
}
