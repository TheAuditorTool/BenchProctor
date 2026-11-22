// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("tracking-service")
export class ValidateProfile {
  @Post("validateProfile")
  async validateProfile(@Req() req: Request): Promise<unknown> {
    const wording = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const parts: string[] = [];
    for (const token of String(wording).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + consignment + "'");
    return { created: true };
  }
}
