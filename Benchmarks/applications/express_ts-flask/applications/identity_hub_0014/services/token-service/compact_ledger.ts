// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const compactLedger = async (req: Request, res: Response): Promise<void> => {
  const snippet = (req.headers.referer as string) || "";
  function normalize(value: string): string { return value.normalize("NFC"); }
  const persona: string = normalize(snippet);
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = ?", [persona]);
  res.json({ accepted: true });
}
