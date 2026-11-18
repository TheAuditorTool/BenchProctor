// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

export const archiveRoster = async (req: Request, res: Response): Promise<void> => {
  const excerpt = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  const capture = (v: string) => (): string => v.trim();
  const readInput = capture(excerpt);
  const handshake: string = readInput();
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + handshake + "'");
  res.json({ accepted: true });
}
