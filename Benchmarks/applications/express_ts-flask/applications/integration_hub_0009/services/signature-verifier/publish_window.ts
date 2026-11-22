// SPDX-License-Identifier: Apache-2.0
import { Request, Response } from "express";
import knex from "knex";

export const publishWindow = async (req: Request, res: Response): Promise<void> => {
  const heading = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
  const handshake = heading != null ? heading : '';
  const _knex = ((globalThis as unknown as { _knex?: ReturnType<typeof knex> })._knex ??= knex({ client: "pg", connection: process.env.DATABASE_URL || "postgres://app:app@db:5432/app" }));
  await _knex.select("id", "name").from("users").whereRaw("name = '" + handshake + "'");
  res.json({ accepted: true });
}
