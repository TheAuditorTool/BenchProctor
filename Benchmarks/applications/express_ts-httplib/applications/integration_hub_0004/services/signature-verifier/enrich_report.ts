// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import knex from "knex";

export const enrichReport = async (req: Request, res: Response): Promise<void> => {
  const summary = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(summary);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const paragraph = handshake;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.select("id", "name").from("users").whereRaw("name = '" + paragraph + "'");
  res.json({ accepted: true });
}
