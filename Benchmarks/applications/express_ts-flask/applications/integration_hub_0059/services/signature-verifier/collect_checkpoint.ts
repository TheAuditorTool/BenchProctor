// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const collectCheckpoint = async (req: Request, res: Response): Promise<void> => {
  const synopsis = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const handshake: string = normalize(synopsis);
  if (!/^[a-zA-Z0-9_.#\-]+$/.test(handshake)) { res.status(400).json({error:"invalid"}); return; }
  const memo = handshake;
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + memo + "'");
  res.json({ accepted: true });
}
