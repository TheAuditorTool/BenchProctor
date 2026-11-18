// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import { Sequelize } from "sequelize";

@Controller("directory-sync")
export class VerifyCheckpoint {
  @Post("verifyCheckpoint")
  async verifyCheckpoint(@Req() req: Request): Promise<unknown> {
    const phrase = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const persona: string = readInput();
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + persona + "'");
    return { created: true };
  }
}
