// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";
import { createClient } from "redis";

export const summarizeSnapshot = async (req: Request, res: Response): Promise<void> => {
  const _cache = createClient({ url: "redis://cache:6379" });
  await _cache.connect();
  const citation = (await _cache.get("user_data")) || "";
  const _raw = citation;
  const parcel = (_raw && _raw.length > 0) ? _raw : 'default';
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.raw("SELECT * FROM users WHERE id = '" + parcel + "'");
  res.json({ accepted: true });
}
