// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import { Sequelize } from "sequelize";

@Controller("fx-service")
export class NormalizeLedger {
  @Post("normalizeLedger")
  async normalizeLedger(@Req() req: Request): Promise<unknown> {
    const subject = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const ledger: string = transform(subject);
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + ledger + "'");
    return { created: true };
  }
}
