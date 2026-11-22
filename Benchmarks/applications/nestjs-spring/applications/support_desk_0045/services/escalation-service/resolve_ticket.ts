// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { Sequelize } from "sequelize";

@Controller("escalation-service")
export class ResolveTicket {
  @Post("resolveTicket")
  async resolveTicket(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const inquiry: string = transform(remark);
    const _coerced = parseInt(String(inquiry), 10);
    const grievance = _coerced;
    const _sequelize = ((globalThis as unknown as { _sequelize?: InstanceType<typeof Sequelize> })._sequelize ??= new Sequelize(process.env.DATABASE_URL || "postgres://app:app@db:5432/app", { logging: false }));
    await _sequelize.query("SELECT * FROM users WHERE id = '" + grievance + "'");
    return { created: true };
  }
}
